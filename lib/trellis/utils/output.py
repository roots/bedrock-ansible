# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os.path
import platform
import re
import textwrap

from ansible import __version__
from ansible import constants as C
from ansible.utils.unicode import to_unicode

def load_configs(obj):
    obj.wrap_width = int(C.get_config(C.p, 'trellis_output', 'wrap_width', 'TRELLIS_WRAP_WIDTH', 80))
    obj.display_include_tasks = (obj._display.verbosity or
        C.get_config(C.p, 'trellis_output', 'display_include_tasks', 'TRELLIS_DISPLAY_INCLUDE_TASKS', False, boolean=True))
    obj.display_skipped_items = (obj._display.verbosity or
        C.get_config(C.p, 'trellis_output', 'display_skipped_items', 'TRELLIS_DISPLAY_SKIPPED_ITEMS', False, boolean=True))
    obj.truncate_items = (not obj._display.verbosity and
        C.get_config(C.p, 'trellis_output', 'truncate_items', 'TRELLIS_TRUNCATE_ITEMS', True, boolean=True))

def system(vagrant_version=None):
    # Get most recent Trellis CHANGELOG entry
    changelog_msg = ''
    ansible_path = os.getenv('ANSIBLE_CONFIG', os.getcwd())
    changelog = os.path.join(ansible_path, 'CHANGELOG.md')

    if os.path.isfile(changelog):
        with open(changelog) as f:
            str = f.read(200)

        # Retrieve release number if it is most recent entry
        release = re.search(r'^###\s((?!HEAD).*)', str)
        if release is not None:
            changelog_msg = '\n  Trellis {0}'.format(release.group(1))

        # Retrieve most recent changelog entry
        else:
            change = re.search(r'.*\n\*\s*([^\(\n\[]+)', str)
            if change is not None:
                changelog_msg = '\n  Trellis at "{0}"'.format(change.group(1).strip())

    # Vagrant info, if available
    vagrant = ' Vagrant {0};'.format(vagrant_version) if vagrant_version else ''

    # Assemble components and return
    return 'System info:\n  Ansible {0};{1} {2}{3}'.format(__version__, vagrant, platform.system(), changelog_msg)

def reset_task_info(obj, task=None):
    obj.action = None if task is None else task._get_parent_attribute('action')
    obj.first_host = True
    obj.first_item = True
    obj.task_failed = False
    obj.vagrant_version = None

# Display dict key only, instead of full json dump
def replace_item_with_key(obj, result):
    if obj.truncate_items:
        if 'key' in result._result['item']:
            result._result['item'] = result._result['item']['key']
        elif 'item' in result._result['item'] and 'key' in result._result['item']['item']:
            result._result['item'] = result._result['item']['item']['key']

# Display item's first line only
def truncate_item(obj, result):
    if obj.truncate_items:
        status = 'changed' if result._result.get('changed', False) else 'ok'
        pre = '{0}: [{1}] => (item=)'.format(status, result._host.get_name())
        item = to_unicode(obj._get_item(result._result))
        if (len(pre) + len(item)) > obj.wrap_width:
            result._result['item'] = '{0}...'.format(item[:(obj.wrap_width - len(pre) - 3)])

def display(obj, result):
    msg = ''
    result = result._result
    display = obj._display.display
    wrap_width = obj.wrap_width
    first = obj.first_host and obj.first_item
    failed = 'failed' in result or 'unreachable' in result

    # Only display msg if debug module or if failed (some modules have undesired 'msg' on 'ok')
    if 'msg' in result and (failed or obj.action == 'debug'):
        msg = result.pop('msg', '')

        # Disable Ansible's verbose setting for debug module to avoid the CallbackBase._dump_results()
        if '_ansible_verbose_always' in result:
            del result['_ansible_verbose_always']

    # Display additional info when failed
    if failed:
        items = (item for item in ['reason', 'module_stderr', 'module_stdout', 'stderr'] if item in result and to_unicode(result[item]) != '')
        for item in items:
            msg = result[item] if msg == '' else '\n'.join([msg, result.pop(item, '')])

        # Add blank line between this fail message and the json dump Ansible displays next
        msg = '\n'.join([msg, ''])

    # Must pass unicode strings to Display.display() to prevent UnicodeError tracebacks
    if isinstance(msg, list):
        msg = '\n'.join([to_unicode(x) for x in msg])
    elif not isinstance(msg, unicode):
        msg = to_unicode(msg)

    # Wrap text
    msg = '\n'.join([textwrap.fill(line, wrap_width, replace_whitespace=False)
                     for line in msg.splitlines()])

    # Display system info and msg, with horizontal rule between hosts/items
    hr = '-' * int(wrap_width*.67)

    if obj.task_failed and first:
        display(system(obj.vagrant_version), 'bright gray')
        display(hr, 'bright gray')

    if msg == '':
        if obj.task_failed and not first:
            display(hr, 'bright gray')
        else:
            return
    else:
        if not first:
            display(hr, 'bright gray')
        display(msg, 'red' if failed else 'bright purple')

def display_host(obj, result):
    if 'results' not in result._result:
        display(obj, result)
        obj.first_host = False

def display_item(obj, result):
    display(obj, result)
    obj.first_item = False
