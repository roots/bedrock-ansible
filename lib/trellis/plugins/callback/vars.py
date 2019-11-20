from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re
import sys

from __main__ import cli
from ansible.module_utils.six import iteritems
from ansible.errors import AnsibleError
from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence, AnsibleUnicode
from ansible.playbook.play_context import PlayContext
from ansible.playbook.task import Task
from ansible.plugins.callback import CallbackBase
from ansible.template import Templar
from ansible.utils.unsafe_proxy import wrap_var


class CallbackModule(CallbackBase):
    ''' Creates and modifies play and host variables '''

    CALLBACK_VERSION = 2.0
    CALLBACK_NAME = 'vars'

    def __init__(self):
        super(CallbackModule, self).__init__()

        # handle Ansible 2.7 and 2.8 cases by normalizing each into a dict
        try:
            from ansible import context
            self._options = context.CLIARGS
        except ImportError:
            self._options = vars(cli.options) if cli else {}

    def raw_triage(self, key_string, item, patterns):
        # process dict values
        if isinstance(item, AnsibleMapping):
            return AnsibleMapping(dict((key,self.raw_triage('.'.join([key_string, key]), value, patterns)) for key,value in iteritems(item)))

        # process list values
        elif isinstance(item, AnsibleSequence):
            return AnsibleSequence([self.raw_triage('.'.join([key_string, str(i)]), value, patterns) for i,value in enumerate(item)])

        # wrap values if they match raw_vars pattern
        elif isinstance(item, AnsibleUnicode):
            match = next((pattern for pattern in patterns if re.match(pattern, key_string)), None)
            return wrap_var(item) if match else item

        else:
            return item

    def raw_vars(self, play, host, hostvars):
        if 'raw_vars' not in hostvars:
            return

        raw_vars = Templar(variables=hostvars, loader=play._loader).template(hostvars['raw_vars'])
        if not isinstance(raw_vars, list):
            raise AnsibleError('The `raw_vars` variable must be defined as a list.')

        patterns = [re.sub(r'\*', '(.)*', re.sub(r'\.', '\.', var)) for var in raw_vars if var.split('.')[0] in hostvars]
        keys = set(pattern.split('\.')[0] for pattern in patterns)
        for key in keys:
            if key in play.vars:
                play.vars[key] = self.raw_triage(key, play.vars[key], patterns)
            elif key in hostvars:
                host.vars[key] = self.raw_triage(key, hostvars[key], patterns)

    def cli_options(self):
        options = []

        strings = {
            '--connection': 'connection',
            '--private-key': 'private_key_file',
            '--ssh-common-args': 'ssh_common_args',
            '--ssh-extra-args': 'ssh_extra_args',
            '--timeout': 'timeout',
            '--vault-password-file': 'vault_password_file',
            }

        for option,value in iteritems(strings):
            if self._options.get(value, False):
                options.append("{0}='{1}'".format(option, str(self._options.get(value))))

        for inventory in self._options.get('inventory'):
            options.append("--inventory='{}'".format(str(inventory)))

        if self._options.get('ask_vault_pass', False):
            options.append('--ask-vault-pass')

        return ' '.join(options)

    def darwin_without_passlib(self):
        if not sys.platform.startswith('darwin'):
            return False

        try:
            import passlib.hash
            return False
        except:
            return True

    def v2_playbook_on_play_start(self, play):
        env = play.get_variable_manager().get_vars(play=play).get('env', '')
        env_group = next((group for key,group in iteritems(play.get_variable_manager()._inventory.groups) if key == env), False)
        if env_group:
            env_group.set_priority(20)

        for host in play.get_variable_manager()._inventory.list_hosts(play.hosts[0]):
            hostvars = play.get_variable_manager().get_vars(play=play, host=host)
            self.raw_vars(play, host, hostvars)
            host.vars['ssh_args_default'] = PlayContext(play=play)._ssh_args.default
            host.vars['cli_options'] = self.cli_options()
            host.vars['cli_ask_pass'] = self._options.get('ask_pass', False)
            host.vars['cli_ask_become_pass'] = self._options.get('become_ask_pass', False)
            host.vars['darwin_without_passlib'] = self.darwin_without_passlib()
