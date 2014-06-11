# bedrock-ansible

[Ansible](http://www.ansible.com/home) [playbook](http://docs.ansible.com/playbooks.html) designed to be used with [Bedrock](http://roots.io/wordpress-stack/) to configure dev & production servers for Bedrock-based WordPress sites.

This playbook will install the common LEMP (Linux/Nginx/MySQL/PHP) stack with PHP 5.5 and [MariaDB](https://mariadb.org/) as a drop-in MySQL replacement (but better) on Ubuntu 14.04 Trusty LTS.

Vagrant is recommended to provision servers and this comes with a basic `Vagrantfile` for an easy dev setup.

## Requirements

1. Ansible >= 1.5.4 - [Installation docs](http://docs.ansible.com/intro_installation.html)
2. Virtualbox >= 4.3.10 - [Downloads](https://www.virtualbox.org/wiki/Downloads)
3. Vagrant >= 1.5.4 - [Downloads](http://www.vagrantup.com/downloads.html)

### OS Notes

From the Ansible docs:

> Currently Ansible can be run from any machine with Python 2.6 installed (Windows isn’t supported for the control machine).
This includes Red Hat, Debian, CentOS, OS X, any of the BSDs, and so on.

If your host machine is running Windows, the workaround is to run Ansible *on the VM* (since it's running Ubuntu) and not locally. This requires some additions to the default `Vagrantfile` and an extra script.

Example `Vagrantfile` for Windows can be found [here](https://gist.github.com/starise/e90d981b5f9e1e39f632/a4b7819b3663c5d34e7c8a2ce4556b50771073e8). There may also be issues with permissions/UAC and symlinks. See this [comment](https://github.com/roots/bedrock-ansible/issues/8#issuecomment-43346116).


## Installation

1. Download/fork/clone this repo to your local machine.
2. Download/fork/clone [Bedrock](https://github.com/roots/bedrock) or have an existing Bedrock-based site ready

You should now have the following directories at the same level somewhere:

```
- bedrock-ansible/
- example.dev/
```

## Usage

1. Edit `Vagrantfile` and set your `config.vm.synced_folder` path so that it points to a local relative path for a Bedrock project from #2 above.
2. Edit `group_vars/all` and add your WordPress site(s). See [Options](#options) below for details.
3. Optionally copy and edit `hosts.example` to `hosts` for more than the single dev host through Vagrant (since Vagrant automatically creates its own hosts inventory).
4. Optionally add any dev hostnames to your local `/etc/hosts` file (or use the [hostsupdated plugin](https://github.com/cogitatio/vagrant-hostsupdater).
5. Run `vagrant up`.

### `Vagrantfile`

The example `Vagrantfile` in this project can be kept in this folder, or moved anywhere else such as a project/site folder. Generally if you want to have multiple sites on 1 Vagrant VM, you should keep the `Vagrantfile` where it is (in the bedrock-ansible dir). If you want to have 1 Vagrant VM *PER* project/site, you should make copies of the `Vagrantfile` and put them into each project's dir. You'd then run `vagrant up` from the project specific directory.

Whenever you move or copy the `Vagrantfile` somewhere else, you need to make sure to adjust the relative paths in it including `config.vm.synced_folder` and `ansible.playbook = './site.yml'`.

## Vagrant Box

By default, the example `Vagrantfile` now uses the `roots/bedrock` box. It's publicly available on the Vagrant Cloud site [here](https://vagrantcloud.com/roots/bedrock).

The `roots/bedrock` box is simply the regular `ubuntu/trustry64` base box already provisioned with this playbook (except for the `wordpress-sites` role). The benefit to using this base box instead of a bare Ubuntu one is that provisioning will be much faster.

Vagrant Cloud offers releases/versions for the boxes, so the `roots/bedrock` box versions will be kept in sync with this project. You can see if there's updates by running `vagrant box outdated` and update it with `vagrant box update`.

Note: you can always set the box back to the base Ubuntu one if you prefer with `config.vm.box = 'ubuntu/trustry64'`

## Options

All Ansible configuration is done in [YAML](http://en.wikipedia.org/wiki/YAML).

### `wordpress_sites`

`wordpress_sites` is the top level array used to define the WordPress sites/virtual hosts that will be created.

* `site_name` (required) - name used to identify site (commonly the domain name) (default: none)
* `site_hosts` (required) - array of hosts that Nginx will listen on (default: none)
* `user` (optional) - user owner of site directories/files (default: `root` | `user` in `site.yml`)
* `group` (optional) - group owner of site directories/files (default: `www-data`)
* `site_install` (optional) - whether to install WordPress or not (default: `true`)
* `site_title` (optional) - WP site title (default: `site_name`)
* `db_import` (optional) - Path to local `sql` dump file which will be imported (default: `false`)
* `system_cron` (optional) - Disable WP cron and use system's (default: `false`)
* `run_composer` (optional) - Run `composer install` before WP install (default: `false`)
* `admin_user` (optional) - WP admin user name (default: `admin`)
* `admin_password` (required if `site_install`) - WP admin user password (default: none)
* `admin_email` (required if `site_install`) - WP admin email address (default: none)
* `multisite` (optional) - hash of multisite options
  * `enabled` (optional) - Multisite enabled flag (default: `false`)
  * `subdomains` (optional) - subdomains option (default: `false`)
  * `base_path` (optional) - base path/current site path (default: `/`)
* `env` (required) - hash of multisite options
  * `wp_home` (required) - `WP_HOME` constant or `home` option (default: none)
  * `wp_siteurl` (required) - `WP_SITEURL` constant or `siteurl` option (default: none)
  * `wp_env` (required) - WordPress environment (default: none)
  * `db_name` (optional) - name of database (default: `site_name`)
  * `db_user` (required) - database user name (default: none)
  * `db_password` (required) - database user password (default: none)
  * `db_host` (required) - database host (default: `localhost`)

### Private Packages

You may want Composer to install packages from private repositories (e.g., a private plugin you've made into a [Composer package](http://roots.io/wordpress-plugins-with-composer/), or a paid plugin you've stored in a private repo). As an alternative to installing your private package from a repository like [Satis](https://getcomposer.org/doc/articles/handling-private-packages-with-satis.md), you may configure this playbook to install private projects that are in your control on hosts such as github or bitbucket:

1. Generate a new ssh key pair (see #2 [here](https://help.github.com/articles/generating-ssh-keys#step-2-generate-a-new-ssh-key)).
2. Add the content of the public key (e.g., `id_rsa.pub`) to each remote private project as a "deploy key" (see deploy keys on [github](https://help.github.com/articles/managing-deploy-keys) or [bitbucket](https://confluence.atlassian.com/display/BITBUCKET/Use+deployment+keys)).
3. Copy the private key file just created (named `id_rsa`) into your bedrock-ansible at `roles/known-hosts/files/id_rsa`. The contents of that folder are gitignored so that private keys won't be committed to your repo.
4. Uncomment the list of `known_hosts` in `group_vars/all` and add your hosts. For example, if you have a private project hosted at github, add `github.com` to the list.

On the occasion a host changes its public key, the ansible play named 'Install Dependencies with Composer' may hang forever when you run `vagrant provision`. Try temporarily setting `flush_known_hosts: true` in `group_vars/all`.

## Todo

* Multisite: basic support is included but not yet complete. There are issues with doing a network install from scratch via WP-CLI.
* MariaDB: there's no `root` password set yet.
* Nginx: configuration needs more options and advanced setups like static files and subdomain multisite support.

