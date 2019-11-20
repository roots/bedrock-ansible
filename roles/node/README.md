# Ansible Role: NVM


Installs NVM & Node.js on Debian/Ubuntu and RHEL/CentOS


Ansible weirdness with SSH and (non)interactive shells makes working with NVM and Ansible a bit problematic. This [stack overflow](https://stackoverflow.com/questions/22256884/not-possible-to-source-bashrc-with-ansible) post explains some of the things other people have done to get around this particular issue.

## Where other roles fall short
Other Ansible roles that install NVM and/or Node.js fall short in a few areas.

1. They use the apt-get or yum packages managers to install Node.js. This often means that the Node.js package is older than what is currently available via the Node.js repo. In some cases, those packages may not be a LTS release and if you need multiple Node.js versions running on the same host, you're out of luck.

1. They will often install NVM and Node.js as `root` user (`sudo su` or `become: true`). This can add to the headache of permissions related to NPM plugin management in addition to being an unneeded privilege escalation security risk

1. You cannot run ad hoc NVM commands


## Where this role differs from other roles

1. You can install NVM via wget, curl or git
1. You can use NVM just like you would via your [command line](https://github.com/creationix/nvm#usage) in your own Ansible tasks and playbooks
1. You can install whatever version or versions of Node.js you want
1. Doesn't install NVM or Node.js as root
1. Can run arbitrary NVM, Node & NPM commands potentially eliminating the need for a separate Node Ansible role all together

## Installation
1. Clone this repo into your roles folder
1. Point the `roles_path` variable to the roles folder i.e. `roles_path = ../ansible-roles/` in your `ansible.cfg` file
1. Include role in your playbook


## Example Playbooks


#### Super Simple
Include the role as is and it will install latest LTS version of Node.js
``` yaml
- hosts: all
  roles:
    - role: ansible-role-nvm
```

#### Simple
Include the role and specify the specific version of Node.js you want to install
``` yaml
- hosts: all
  roles:
    - role: ansible-role-nvm
      nodejs_version: "8.15.0"

```
#### More Complex
This example shows how you might set up multiple environments (Dev/Prod) with different options. The Prod setup takes advantage of the `nvm_commands` option to install, build and run the application. The role supports and takes advantage of Ansible variable syntax e.g. `{{ variable_name }}`.
``` yaml
- hosts: dev
  vars_files:
    - vars/dev.yml
  roles:
    - role: ansible-role-nvm
      nodejs_version: "{{ config.dev.nodejs.version }}"


- hosts: prod
  vars_files:
    - vars/prod.yml
  roles:
    - role: ansible-role-nvm
      nvm_install: "curl"
      nvm_dir: "/usr/local/nvm"
      nvm_commands:
       - "nvm install {{ config.prod.client-1.nodejs.version }}"
       - "nvm alias default {{ config.prod.client-1.nodejs.version }}"
       - "nvm exec default npm install"
       - "nvm exec default npm run prod"

```

## Installing/Running/Maintaining or Upgrading multiple versions of Node.js on the same host

By default, the **first** Node.js version instantiated in your Playbook will automatically be aliased as the "default" version regardless of whatever version you install afterwards or how many times you run the role. It is important to declare which version is expected to be the "default" version.

There are two NVM aliases `default` (current "active" version of Node.js) and `system` (the base OS version of Node.js). *Aliasing is a very powerful feature of NVM and it is a recommended best practice for managing your environment*.


``` yaml

- hosts: host-1
  roles:
    # Services
    - role: ansible-role-nvm
      nodejs_version: "8.15.0"    # <= This will be the "default" version of Node.js

    # Application
    - role: ansible-role-nvm
      nodejs_version: "10.15.0"

```


``` yaml

- hosts: host-2
  roles:
    # Services
    - role: ansible-role-nvm
      nodejs_version: "8.15.0"    

    # Application
    - role: ansible-role-nvm
      default: true
      nodejs_version: "10.15.0" # <= This is now the "default" version of Node.js

```

<a name='#nvm-commands'></a>
## Notes on NVM commands
**NVM commands are a very powerful feature of this role** which takes advantage of the groundwork NVM has set up. Leveraging `nvm_commands` could potentially eliminate the need for a specific Node role to manage your Node applications.

`nvm run` and `nvm exec` can be used as aliases for the `node` and `npm` command line commands.

`nvm exec default npm run server` is functionally equivalent to `npm run server` where `server` is some json key in the scripts block of your package.json file e.g.

``` json
{
  "name": "my_application",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "preserver": "npm run dbService &",
    "server": "nodemon ./bin/www",
    "build": "node build/build.js",
    "dbService": "nodemon ./data-service/server.js --ignore node_modules/"
  },
  "dependencies": {
  }
}
```
`nvm_commands` make it easy to set up a Node Application and Node API layer running on different version of Node.js on the same host

``` yaml

- hosts: host-1
  roles:
    # Services
    # WHAT'S HAPPENING?
    # 1. Run the services script in your package.json file with Node version 8.15.0
    # WARNING: This is aliased as the default version of Node.js At this point !!
    # Therefore We need to explicitly specify the version we're using because
    # the default Node.js version changes in Application section below
    - role: ansible-role-nvm
      nodejs_version: "8.15.0"
      nvm_commands:
        - "nvm exec 8.15.0 npm run services"

    # Application
    # WHAT'S HAPPENING?
    # 1. Set the default version of Node.js to version 10.15.0
    # 2. Run the test scripts (using the default alias version of 10.15.0)
    # 3. Then run the production deploy script
    - role: ansible-role-nvm
      nodejs_version: "10.15.0"
      nvm_commands:
       - "nvm alias default {{ nodejs_version }}" # <= Changes the default NVM version (supports Ansible variable syntax)
       - "nvm exec default node run test" # invoke Node.js directly to run the test script in package.json file
       - "nvm exec default npm run default prod" # invoke npm to run the production script in your package.json file

```
Another example

``` yaml

- hosts: host-2
  roles:
    # Services
    # WHAT'S HAPPENING?
    # 1. Create an Alias for version 8.15.0 entitled service-default (Supports Ansible variable syntax)
    # 2. Run the services script
    #
    # ** It is recommended that you alias your Node.js versions and reference them accordingly **
    - role: ansible-role-nvm
      nodejs_version: "8.15.0"
      nvm_commands:
        - "nvm alias service-default {{ nodejs_version }}" # <= (Supports Ansible variable syntax)
        - "nvm exec service-default npm run services" # run the services script in your package.json file


    # Application - No spearate Node.js Ansible Role Needed
    # WHAT'S HAPPENING?
    # 1. Install version 10.15.0 of Node.js
    # 1. Set the default version of Node.js to version 10.15.0
    # 2. Run the test.js script file invoking Node.js directly
    # 3. Then run the production deploy bash script
    - role: ansible-role-nvm
      nvm_commands:
       - "nvm install 10.15.1"
       - "nvm alias default 10.15.1" # <= Changes the default NVM version
       - "nvm exec default node run test.js" # invoke Node.js directly to run the test script in package.json file
       - "nvm exec ./deploy.sh" # run an arbitrary bash script

```

**Whatever command line arguments you use to start your application, or command scripts you've declared in your package.json file can be placed inside the `nvm_commands: []` section of this role.**

*There is a difference between `nvm run` and `nvm exec` commands. You can think of `nvm run` as functionally equivalent to `node run server.js` or `node server.js` where you are invoking a server.js script file. `nvm exec` executes in a sub process context and is functionally equivalent to `npm run server` where `server` is a key name in the scripts section in the package.json file. They are both valid use cases for `nvm_commands` options*


## Caveats

1. By default, the **first** version listed in your Playbook, on the **first** run, will automatically be aliased as the "default" version of Node.js regardless of whatever version you install afterwards or however many times you run the role. First one in/installed is always the default. As a result, if you expect a Node.js version declared later in the playbook to be set as default use `default: True` or explicitly set it in the `nvm_commands` list like `- "nvm alias default <YOUR_VERSION>"`

1. If you have `default: True` as a role variable **AND** `- "nvm alias default <SOME_OTHER_VERSION>"` as part of your `nvm_commands` the version with `default: True` will **ALWAYS** be executed **first**. This is because we need Node.js to be available before doing anything else.  

1. NVM is stateless in that if you have multiple versions of Node.js installed on a machine, you may have to run `nvm use <VERSION>` as part of your script to run the Node.js version you want/expect. However, it is higly recommended that you alias your versions accordingly and reference them that way. See the example above.

## Issues
If you are getting a `"cannot find /usr/bin/python"` error. It is due to OS's that run Python 3 by default (e.g. Fedora). You will need to specify the Ansible python interpreter variable in the inventory file or via the command line

```
[fedora1]
192.168.0.1 ansible_python_interpreter=/usr/bin/python3


[fedora2]
192.168.0.2

[fedora2:vars]
ansible_python_interpreter=/usr/bin/python3

```
or
```
ansible-playbook my-playbook.yml -e "ansible_python_interpreter=/usr/bin/python3"
```







## Role Variables

Available variables are listed below, along with default values see [defaults/main.yml]( defaults/main.yml)

The Node.js version to install. The latest "lts" version is the default and works on most supported OSes.

    nodejs_version: "lts"

Convenience method for installing NVM bash autocomplete (`nvm <TAB>`) when a user has to maintain a server manually

    autocomplete: False


Set default version of Node when maintaining/installing multiple versions

    default: False

*NVM will automatically alias the first run/installed version as "default" which is more than likely what people will use this role  for, however, this will allow for installation/upgrade of multiple versions on an existing machine*


List of [NVM commands to run](https://github.com/creationix/nvm#usage). Default is an empty list.

    nvm_commands: []

NVM Installation type. Options are wget, curl and git

    nvm_install: "wget"

NVM Installation directory.

    nvm_dir: ""

*NVM will, by default, install the `.nvm` directory in the home directory of the user e.g. `/home/user1/.nvm`. You can override the installation directory by changing this variable e.g. `/opt/foo/nvm`. This variable will respect Ansible substitution variables e.g. `{{ansible_env.HOME}}`*

NVM Profile location Options are .profile, .bashrc, .bash_profile, .zshrc

    nvm_profile: ".bashrc"

NVM source location i.e. you host your own fork of [NVM](https://github.com/creationix/nvm)

    nvm_source: ""


NVM version to install

    nvm_version: "0.35.0"


Uninstall NVM, will remove .nvm directory and clean up `{{ nvm_profile }}` file

    uninstall: False




## Dependencies

None.

## Change Log

**1.2.2**
* NVM version bump

**1.2.1**
* Documentation updates for clarity

**1.2.0**
* Addresses issues [#8 Add default: True role variable to ensure NVM default alias is set correctly](https://github.com/morgangraphics/ansible-role-nvm/issues/8), [#9 Git functionality has changed according to the NVM documentation](https://github.com/morgangraphics/ansible-role-nvm/issues/9), [#10 NVM has an Autocomplete functionality. Add `autocomplete: True` Ansible variable to role](https://github.com/morgangraphics/ansible-role-nvm/issues/10), [#11 Update documentation to highlight updating a default version](https://github.com/morgangraphics/ansible-role-nvm/issues/11), and [#12 Add remove: True variable to uninstall NVM ](https://github.com/morgangraphics/ansible-role-nvm/issues/12) as discussed with [@DanHulton](https://github.com/morgangraphics/ansible-role-nvm/pull/7) to address multiple version of Node.js running on the same host.
* Expanded documentation with examples about how powerful `nvm_commands: []` can be

**1.1.2**
* Issue reported/PR supplied by [@DanHulton](https://github.com/morgangraphics/ansible-role-nvm/pull/5), Documentation updates,

**1.1.1**
* Documentation updates

**1.1.0**
* Issue reported by [@magick93](https://github.com/morgangraphics/ansible-role-nvm/issues/3), Bumped default version of NVM script, Documentation updates

**1.0.2**
* Issue reported by [@swoodford](https://github.com/morgangraphics/ansible-role-nvm/issues/1), Bumped default version of NVM script, Documentation updates

## License

MIT / BSD

## Author Information

dm00000 via MORGANGRAPHICS, INC

This role borrows heavily from [Jeff Geerling's](https://www.jeffgeerling.com/) Node.js role, author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
