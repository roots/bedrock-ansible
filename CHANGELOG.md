### Head
* wordpress-setup: Block dependency manager files by Nginx ([#1116](https://github.com/roots/trellis/pull/1116))

### 1.2.0: October 11th, 2019
* Lets Encrypt ACME v2 support ([#1114](https://github.com/roots/trellis/pull/1114))
* Fix self-signed certificates in Ansible 2.8 ([#1110](https://github.com/roots/trellis/pull/1110))
* Update WP CLI to v2.3.0 ([#1109](https://github.com/roots/trellis/pull/1109))
* Ansible 2.8.x support ([#1103](https://github.com/roots/trellis/pull/1103))
* Bump galaxy dependency versions ([#1105](https://github.com/roots/trellis/pull/1105))
* Fix issues with Vagrant ansible_local provisioner ([#1104](https://github.com/roots/trellis/pull/1104))
* Bump ansible requirement to 2.7.12([#1102](https://github.com/roots/trellis/pull/1102))

### 1.1.0: September 1st, 2019
* Update swapfile role to v2.0.22 ([#1101](https://github.com/roots/trellis/pull/1101))
* Add pip `requirements.txt` and rename `requirements.yml` to `galaxy.yml` ([#1100](https://github.com/roots/trellis/pull/1100))
* Update apt packages before checking essentials task ([#1086](https://github.com/roots/trellis/pull/1086))
* Setup composer HTTP basic authentication for multiple repositories ([#1091](https://github.com/roots/trellis/pull/1091))

### 1.0.3: April 30th, 2019
* Prevent direct access for `.blade.php` files ([#1075](https://github.com/roots/trellis/pull/1075))
* Show custom error message if external IP resolution fails ([#1078](https://github.com/roots/trellis/pull/1078))
* Use all canonical site hosts for Landrush TLD ([#1077](https://github.com/roots/trellis/pull/1077))

### 1.0.2: March 13th, 2019
* Improve handling of vars with `AnsibleUnsafe` ([#1071](https://github.com/roots/trellis/pull/1071))
* Update name of Nginx PPA (`development` to `mainline`) ([#1068](https://github.com/roots/trellis/pull/1068))
* [REVERT] Don't force install Ansible Galaxy in dev ([#1064](https://github.com/roots/trellis/pull/1064))

### 1.0.1: January 16th, 2019
* Add Python 2 explicitly ([#1061](https://github.com/roots/trellis/pull/1061))

### 1.0.0: December 27th, 2018
* Hyper-V and SMB folder sync compatibility ([#1035](https://github.com/roots/trellis/pull/1035))
* Use Ruby script for ssh-config trigger ([#1053](https://github.com/roots/trellis/pull/1053))
* Update to PHP 7.3 ([#1052](https://github.com/roots/trellis/pull/1052))
* Enable per-user `update_password` behavior ([#767](https://github.com/roots/trellis/pull/767))
* Fix Vagrant trigger path ([#1051](https://github.com/roots/trellis/pull/1051))
* Fix: `vault_wordpress_env_defaults` not populated during deploy ([#1049](https://github.com/roots/trellis/pull/1049))
* Add `vault_wordpress_env_defaults` ([#1048](https://github.com/roots/trellis/pull/1048))
* Allow overriding rollback variables ([#1047](https://github.com/roots/trellis/pull/1047))
* Require Vagrant >= 2.1.0 ([#1046](https://github.com/roots/trellis/pull/1046))
* Bump Ansible `version_tested_max` to 2.7.5 ([#1045](https://github.com/roots/trellis/pull/1045))
* Add Vagrant `ssh-config` to `~/.ssh/config` on `vagrant up` ([#1042](https://github.com/roots/trellis/pull/1042))
* [BREAKING] Add Ubuntu 18.04 support and default to it ([#992](https://github.com/roots/trellis/pull/992))
* Python 3 support ([#1031](https://github.com/roots/trellis/pull/1031))
* Allow customizing Nginx `worker_connections` ([#1021](https://github.com/roots/trellis/pull/1021))
* Update wp-cli to 2.0.1 ([#1019](https://github.com/roots/trellis/pull/1019))
* [BREAKING] Update wp-cli to 2.0.0 and verify its PGP signature ([#1014](https://github.com/roots/trellis/pull/1014))
* Deploy: Remove obsoleted `git` remote checking ([#999](https://github.com/roots/trellis/pull/999))
* Update xdebug tunnel configuration ([#1007](https://github.com/roots/trellis/pull/1007))
* Verify `wp-cli.phar` checksum ([#996](https://github.com/roots/trellis/pull/996))
* Enable `fastcgi_cache_background_update` by default ([#962](https://github.com/roots/trellis/pull/962))
* Bump Ansible `version_tested_max` to 2.5.3 ([#981](https://github.com/roots/trellis/pull/981))
* deploy.sh: Return non-zero exit code when misuse  ([#990](https://github.com/roots/trellis/pull/990))
* Add CSP `frame-ancestors`, make `X-Frame-Options` conditional ([#977](https://github.com/roots/trellis/pull/977))
* Common: Install `git` instead of `git-core`  ([#989](https://github.com/roots/trellis/pull/989))
* Add `xdebug.remote_autostart` to simplify xdebug sessions  ([#985](https://github.com/roots/trellis/pull/985))
* Enable nginx to start on boot ([#980](https://github.com/roots/trellis/pull/980))
* Update geerlingguy.ntp 1.5.2->1.6.0 ([#984](https://github.com/roots/trellis/pull/984))
* Update geerlingguy.composer 1.6.1->1.7.0 ([#983](https://github.com/roots/trellis/pull/983))
* Update wp-cli to 1.5.1 ([#982](https://github.com/roots/trellis/pull/982))
* Support git url format `ssh://user@host/path/to/repo` ([#975](https://github.com/roots/trellis/pull/975))
* Fix path to h5bp/mime.types ([#974](https://github.com/roots/trellis/pull/974))
* Vendor h5bp Nginx configs ([#973](https://github.com/roots/trellis/pull/973))
* Add support for sSMTP revaliases configuration ([#956](https://github.com/roots/trellis/pull/956))
* Add support for includes.d on all sites ([#966](https://github.com/roots/trellis/pull/966))
* Fix `--subdomains` flag in the Install WP task ([#968](https://github.com/roots/trellis/pull/968))
* Ensure Diffie-Hellman group is generated for Let's Encrypt ([#964](https://github.com/roots/trellis/pull/964))
* Fix `raw_vars` feature to properly handle int values ([#959](https://github.com/roots/trellis/pull/959))
* [BREAKING] Update Ansible default plugin paths in config files ([#958](https://github.com/roots/trellis/pull/958))
* Add Nginx `ssl.no-default.conf` to drop requests for unknown hosts ([#888](https://github.com/roots/trellis/pull/888))
* [BREAKING] Disable memcached UDP support by default ([#955](https://github.com/roots/trellis/pull/955))
* Git: Ignore `vagrant.local.yml`([#953](https://github.com/roots/trellis/pull/953))
* Update to PHP 7.2 ([#929](https://github.com/roots/trellis/pull/929))
* Fix `failed_when` in `template_root` check with wp-cli 1.5.0 ([#948](https://github.com/roots/trellis/pull/948))
* Bump Ansible `version_tested_max` to 2.4.3.0 ([#945](https://github.com/roots/trellis/pull/945))
* Update wp-cli to 1.5.0 ([#944](https://github.com/roots/trellis/pull/944))
* Update `vagrant_box_version` to `>= 201801.02.0` ([#939](https://github.com/roots/trellis/pull/939))
* Bump Ansible `version_tested_max` to 2.4.2.0 ([#932](https://github.com/roots/trellis/pull/932))
* Add MariaDB 10.2 PPA ([#926](https://github.com/roots/trellis/pull/926))
* Switch from `.dev` to `.test` ([#923](https://github.com/roots/trellis/pull/923))

### 1.0.0-rc.2: November 13th, 2017
* Update wp-cli to 1.4.1 ([#918](https://github.com/roots/trellis/pull/918))
* Disallow duplicate site keys within a host's `wordpress_sites` ([#910](https://github.com/roots/trellis/pull/910))
* Fix `raw_vars` functionality for Ansible 2.4.1 ([#915](https://github.com/roots/trellis/pull/915))
* Enable Virtualbox ioapic option ([#913](https://github.com/roots/trellis/pull/913))
* Dynamically increase `ansible_group_priority` for selected env ([#909](https://github.com/roots/trellis/pull/909))
* Bump Ansible `version_tested_max` to 2.4.1.0 ([#911](https://github.com/roots/trellis/pull/911))
* Update wp-cli to 1.4.0 ([#906](https://github.com/roots/trellis/pull/906))
* [BREAKING] Normalize `apt` tasks ([#881](https://github.com/roots/trellis/pull/881))
* Ansible 2.4 compatibility ([#895](https://github.com/roots/trellis/pull/895))
* Default h5bp expires and cache busting to false ([#894](https://github.com/roots/trellis/pull/894))
* Deploys: Update WP theme paths for multisite subsites ([#854](https://github.com/roots/trellis/pull/854))
* Vagrant: Support DHCP ([#892](https://github.com/roots/trellis/pull/892))
* Extract Trellis::Config ([#890](https://github.com/roots/trellis/pull/890))
* Redirect directly to https canonical domain ([#889](https://github.com/roots/trellis/pull/889))
* WordPress Setup: Add Nginx `ssl_client_certificate` ([#869](https://github.com/roots/trellis/pull/869))
* Update h5bp/server-configs-nginx ([#876](https://github.com/roots/trellis/pull/876))
* Update ansible galaxy roles ([#872](https://github.com/roots/trellis/pull/872))
* Update wp-cli to 1.3.0 ([#871](https://github.com/roots/trellis/pull/871))
* Add ansible_local support for non-Windows ([#824](https://github.com/roots/trellis/pull/824))
* Load `modules-enabled` config files in Nginx ([#859](https://github.com/roots/trellis/pull/859))
* Only include \*.conf files in Nginx `sites-enabled/` ([#862](https://github.com/roots/trellis/pull/862))
* Add `fastcgi_read_timeout` to Nginx config ([#860](https://github.com/roots/trellis/pull/860))
* Allow customization of the Nginx package name and PPA ([#858](https://github.com/roots/trellis/pull/858))
* Nginx microcaching: skip caching WP API requests ([#855](https://github.com/roots/trellis/pull/855))
* Allow overriding more php-fpm params ([#856](https://github.com/roots/trellis/pull/856))
* Accommodate child themes: Update WP `stylesheet_root` separately ([#850](https://github.com/roots/trellis/pull/850))
* Deploys: `--skip-themes` when updating WP `template_root` ([#849](https://github.com/roots/trellis/pull/849))
* Option to install WP-CLI packages ([#837](https://github.com/roots/trellis/pull/837))
* Update WP-CLI to 1.2.1 ([#838](https://github.com/roots/trellis/pull/838))
* Auto-install Vagrant plugins ([#829](https://github.com/roots/trellis/pull/829))
* Add Vagrant config ([#828](https://github.com/roots/trellis/pull/828))
* Ansible 2.3 compatibility ([#813](https://github.com/roots/trellis/pull/813))
* Remove potentially dangerous `db_import` option ([#825](https://github.com/roots/trellis/pull/825))

### 1.0.0-rc.1: April 7th, 2017
* Add vault_wordpress_sites validation ([#823](https://github.com/roots/trellis/pull/823))
* Use dynamic HostKeyAlgorithms SSH option for unknown hosts ([#798](https://github.com/roots/trellis/pull/798))
* Accommodate deploy hook vars formatted as lists of includes ([#815](https://github.com/roots/trellis/pull/815))
* Check Ansible version before Ansible validates task attributes ([#797](https://github.com/roots/trellis/pull/797))
* Add additional Nginx sites configurations support ([#793](https://github.com/roots/trellis/pull/793))
* Change `remote-user` role to `connection` role: tests host key, user ([#745](https://github.com/roots/trellis/pull/745))
* Allow customization of PHP extensions ([#787](https://github.com/roots/trellis/pull/787))
* Allow for per-project packagist.com authentication ([#762](https://github.com/roots/trellis/pull/762))
* Set multisite constants false while checking `wp core is-installed` ([#766](https://github.com/roots/trellis/pull/766))
* Forward extra bin/deploy.sh parameters to ansible-playbook ([#748](https://github.com/roots/trellis/pull/748))
* Update WP-CLI to 1.1.0 ([#759](https://github.com/roots/trellis/pull/759))
* Add DOMAIN_CURRENT_SITE to default env variables ([#760](https://github.com/roots/trellis/pull/760))
* Fix formatting of `set_fact` for `ansible_become_pass` ([#758](https://github.com/roots/trellis/pull/758))
* Require Ansible 2.2.0.0 or greater ([#726](https://github.com/roots/trellis/pull/726))
* [BREAKING] Use more secure sshd defaults ([#744](https://github.com/roots/trellis/pull/744))
* Add basic git repo host keys to `known_hosts` ([#751](https://github.com/roots/trellis/pull/751))
* Accommodate template inheritance for nginx confs ([#740](https://github.com/roots/trellis/pull/740))
* Add `apt_packages_custom` to customize Apt packages ([#735](https://github.com/roots/trellis/pull/735))
* Enable Let's Encrypt to detect updated `site_hosts` ([#630](https://github.com/roots/trellis/pull/630))
* Add `SKIP_GALAXY` env var to skip galaxy install in Vagrant ([#734](https://github.com/roots/trellis/pull/734))
* Avoid `loop.first` variable in conditional jinja loops ([#729](https://github.com/roots/trellis/pull/729))
* Use dynamic `local_path` to accommodate Ansible running on VM ([#725](https://github.com/roots/trellis/pull/725))
* [BREAKING] Fix #727 - HSTS: default preload to off ([#728](https://github.com/roots/trellis/pull/728))
* `Vagrantfile`: add automatic support for landrush ([#724](https://github.com/roots/trellis/pull/724))
* Suppress extra output in SSL certificates ([#723](https://github.com/roots/trellis/pull/723))
* Fix #718 - improve method of updating theme paths ([#720](https://github.com/roots/trellis/pull/720))
* Create `/home/vagrant/trellis` bindfs mount with proper permissions ([#705](https://github.com/roots/trellis/pull/705))

### 0.9.9: December 14th, 2016
* Create `project_shared_children` files if they do not exist ([#706](https://github.com/roots/trellis/pull/706))
* Diffie-Hellman params now conditional on SSL status ([#709](https://github.com/roots/trellis/pull/709))
* Update PHP to 7.1 ([#695](https://github.com/roots/trellis/pull/695))
* Update WP-CLI to 1.0.0 ([#708](https://github.com/roots/trellis/pull/708))
* Ansible-Local for Vagrant boxes on Windows ([#690](https://github.com/roots/trellis/pull/690))
* Install MariaDB via Ubuntu's official distro packages ([#693](https://github.com/roots/trellis/pull/693))
* Fix 404s by moving skip_cache conditions to server block ([#692](https://github.com/roots/trellis/pull/692))
* Nginx includes: Move templates dir, fix 'No such file' error ([#687](https://github.com/roots/trellis/pull/687))
* [BREAKING] Move shell scripts to bin/ directory ([#680](https://github.com/roots/trellis/pull/680))
* Add myhostname to nsswitch.conf to ensure resolvable hostname ([#686](https://github.com/roots/trellis/pull/686))
* Add `bin/xdebug-tunnel.sh` to manage Xdebug and SSH tunnels on remote hosts ([#678](https://github.com/roots/trellis/pull/678))
* Move Xdebug installation/configuration into its own role ([#678](https://github.com/roots/trellis/pull/678))
* Disable wp-cron emails ([#685](https://github.com/roots/trellis/pull/685))
* Make `raw_vars` compatible with play vars and Ansible 2.1 ([#684](https://github.com/roots/trellis/pull/684))
* Ensure there is always at least one PHP-FPM pool defined ([#682](https://github.com/roots/trellis/pull/682))
* Update galaxy roles for Ansible 2.2 compatibility ([#681](https://github.com/roots/trellis/pull/681))
* Update to WP-CLI 0.25.0 for WP 4.7 compat ([#673](https://github.com/roots/trellis/pull/673))
* Enable per-site setup for permalink structure ([#661](https://github.com/roots/trellis/pull/661))
* WP 4.6 Compat: set WP_HOME/SITEURL directly ([#647](https://github.com/roots/trellis/pull/647))
* Create WordPress php-fpm conf after web_root exists ([#642](https://github.com/roots/trellis/pull/642))
* Fix #637 - Fix condition for permalink structure task ([#643](https://github.com/roots/trellis/pull/643))
* Fix #639 - WP 4.6 compatibility: update WP-CLI to 0.24.1 ([#640](https://github.com/roots/trellis/pull/640))

### 0.9.8: August 14th, 2016
* Ansible 2.1 compatibility fixes ([#631](https://github.com/roots/trellis/pull/631))
* [BREAKING] Upgrade Ubuntu from 14.04 Trusty to 16.04 Xenial ([#626](https://github.com/roots/trellis/pull/626))
* [BREAKING] Add `vault_users` for easier password management ([#614](https://github.com/roots/trellis/pull/614))
* Fix #581 - Use WP-CLI to run WP cron ([#583](https://github.com/roots/trellis/pull/583))
* [BREAKING] Require explicit redirects and drop `www_redirect` ([#622](https://github.com/roots/trellis/pull/622))
* Fix #612 - Bump nginx_fastcgi_buffer_size to `8k` ([#620](https://github.com/roots/trellis/pull/620))
* Setup permalink structure for multisite installs too ([#617](https://github.com/roots/trellis/pull/617))
* Fix `wp_home` option in Multisite after install in development ([#616](https://github.com/roots/trellis/pull/616))
* Add `current_path` var and default to enable custom current release path ([#607](https://github.com/roots/trellis/pull/607))
* Add Vagrant post up message ([#602](https://github.com/roots/trellis/pull/602))
* Fix #468 - Use curl to install wp-cli tab completions ([#593](https://github.com/roots/trellis/pull/593))
* Require Ansible 2.0.2 and remove deploy_helper ([#579](https://github.com/roots/trellis/pull/579))
* Add connection-related cli options to ping command ([#578](https://github.com/roots/trellis/pull/578))
* Wrap my.cnf password in quotes ([#577](https://github.com/roots/trellis/pull/577))
* Update to WP-CLI v0.23.1 ([#576](https://github.com/roots/trellis/pull/576))
* Fix #563 - Improve remote databases ([#573](https://github.com/roots/trellis/pull/573))
* Fix #569 - Only skip subdomains for non-www domains ([#570](https://github.com/roots/trellis/pull/570))
* Enable Let's Encrypt to transition http sites to https ([#565](https://github.com/roots/trellis/pull/565))

### 0.9.7: April 10th, 2016
* Fix #550 - Properly skip permalink setup for MU ([#551](https://github.com/roots/trellis/pull/551))
* Escape salts and keys to avoid templating errors ([#548](https://github.com/roots/trellis/pull/548))
* Add plugin to pretty print Ansible msg output ([#544](https://github.com/roots/trellis/pull/544))
* Fix #482 - Multisite is-installed deploy check ([#543](https://github.com/roots/trellis/pull/543))
* Skip setting permalink for multisite installs ([#546](https://github.com/roots/trellis/pull/546))
* Fix #489 - Add $realpath_root to fastcgi_cache_key ([#542](https://github.com/roots/trellis/pull/542))
* Move modules and plugins to `lib/trellis` directory ([#538](https://github.com/roots/trellis/pull/538))
* Automatically set `wp_home` and `wp_siteurl` variables ([#533](https://github.com/roots/trellis/pull/533))
* Switch to Let's Encrypt X3 intermediate certificate and fix chain issues ([#534](https://github.com/roots/trellis/pull/534))
* Supply better defaults for `db_name` and `db_user` ([#529](https://github.com/roots/trellis/pull/529))
* Fix deploy env template to use valid ansible vars ([#530](https://github.com/roots/trellis/pull/530))
* Simplify and improve `wordpress_sites` with better defaults ([#528](https://github.com/roots/trellis/pull/528))
* Allow option for WinNFSD sync folder provider on Windows ([#527](https://github.com/roots/trellis/pull/527))
* Improve Let's Encrypt challenge pre-flight tests ([#526](https://github.com/roots/trellis/pull/526))
* `reverse_www` filter improvements (ignore subdomains) ([#525](https://github.com/roots/trellis/pull/525))
* Fix deprecation warnings on deploy, use current stable WP-CLI ([#523](https://github.com/roots/trellis/pull/523))
* Fix #520 - Disable MariaDB binary logging by default ([#521](https://github.com/roots/trellis/pull/521))
* Let's Encrypt integration ([#518](https://github.com/roots/trellis/pull/518))
* Improve Git repo format validation ([#516](https://github.com/roots/trellis/pull/516))
* Fix #505 - Git ignore \*.retry file
* Fix Ansible deprecations for bare variables ([#510](https://github.com/roots/trellis/pull/510))
* Fixes #508 - update php-xdebug config file path ([#509](https://github.com/roots/trellis/pull/509))
* Add php-mbstring extension ([#504](https://github.com/roots/trellis/pull/504))
* Add more necessary PHP extensions ([#503](https://github.com/roots/trellis/pull/503))

### 0.9.6: February 18th, 2016
* Update to latest ansible-role-mailhog version ([#497](https://github.com/roots/trellis/pull/497))
* Add `reverse_www` filter to fix `www_redirect` ([#486](https://github.com/roots/trellis/pull/486))
* Add IP address variable, move some variables to top of Vagrantfile ([#494](https://github.com/roots/trellis/pull/494))
* Keep Composer updated ([#493](https://github.com/roots/trellis/pull/493))
* Use prestissimo Composer plugin ([#492](https://github.com/roots/trellis/pull/492))
* Use ansible-role-composer ([#491](https://github.com/roots/trellis/pull/491))
* Fix bad `curl` output ([#490](https://github.com/roots/trellis/pull/490))
* Fixes #410 - Default to 1 CPU in Vagrant ([#487](https://github.com/roots/trellis/pull/487))

### 0.9.5: February 10th, 2016
* Fix Nginx includes for Ansible 2.0 ([#473](https://github.com/roots/trellis/pull/473))
* Use `ondrej/php` PPA since `ondrej/php-7.0` is deprecated ([#479](https://github.com/roots/trellis/pull/479))
* Fix Ansible 2.x deploys and require version 2.x ([#478](https://github.com/roots/trellis/pull/478))
* Update to PHP 7.0 and remove HHVM ([#432](https://github.com/roots/trellis/pull/432))
* Windows: Sync `hosts` dir with proper permissions ([#460](https://github.com/roots/trellis/pull/460))
* Fix `inventory_file` variable in connection tests ([#470](https://github.com/roots/trellis/pull/470))
* Fix conditional logic for permalink setup task ([#467](https://github.com/roots/trellis/pull/467))
* Fix permalink setup during WordPress Install ([#466](https://github.com/roots/trellis/pull/466))
* Fix deploy pre-flight check for verifying repo ([#463](https://github.com/roots/trellis/pull/463))
* Ansible 2.0 compatibility ([#461](https://github.com/roots/trellis/pull/461))
* Add pre-flight checks for common deploy problems ([#459](https://github.com/roots/trellis/pull/459))
* Prevent duplicate hosts entries made by `vagrant-hostsupdater` ([#458](https://github.com/roots/trellis/pull/458))
* Fix README's `ansible-playbook` command for server.yml ([#456](https://github.com/roots/trellis/pull/456))
* Fix development hosts file ([#455](https://github.com/roots/trellis/pull/455))
* Add tags to select includes and tasks ([#453](https://github.com/roots/trellis/pull/453))
* Improve Git deploy implementation via `git archive` ([#451](https://github.com/roots/trellis/pull/451))
* Replace strip_www with optional redirect to www/non-www ([#452](https://github.com/roots/trellis/pull/452))
* Accommodate file encryption via ansible vault ([#317](https://github.com/roots/trellis/pull/317))
* Fixes #353 - Allow insecure curl reqs for cron ([#450](https://github.com/roots/trellis/pull/450))
* Fixes #374 - Remove composer vendor/bin from $PATH ([#449](https://github.com/roots/trellis/pull/449))
* Refactor hosts files ([#313](https://github.com/roots/trellis/pull/313))
* Fixes #436 - Let WP handle 404s for PHP files ([#448](https://github.com/roots/trellis/pull/448))
* Fixes #297 - Use `php_flag` vs `php_admin_flag` ([#447](https://github.com/roots/trellis/pull/447))
* Fixes #316 - Set WP permalink structure during install ([#316](https://github.com/roots/trellis/pull/316))
* Switch to https://api.ipify.org for IP lookup ([#444](https://github.com/roots/trellis/pull/444))
* Replace `vagrant-hostsupdater` with `vagrant-hostmanager` ([#442](https://github.com/roots/trellis/pull/442))
* Switch to mainline Nginx, replaces SPDY with HTTP2 ([#389](https://github.com/roots/trellis/issues/389))
* Add `wp core update-db` to deploy finalize hook ([#411](https://github.com/roots/trellis/pull/411))
* Use WP-CLI 0.21.1 ([#392](https://github.com/roots/trellis/pull/392))
* Add variable for whitelisted IPs ([#435](https://github.com/roots/trellis/pull/435))

### 0.9.3: November 29th, 2015
* Nginx role improvements: use more h5bp configs ([#428](https://github.com/roots/trellis/pull/428))
* Add global `deploy_before` and `deploy_after` hooks ([#427](https://github.com/roots/trellis/pull/427))
* Fix HSTS headers ([#424](https://github.com/roots/trellis/pull/424))
* Notify Windows users about SSH forwarding ([#423](https://github.com/roots/trellis/pull/423))
* Use append_privs for WP DB privileges ([#422](https://github.com/roots/trellis/pull/422))
* Stop WP cron job emails ([#421](https://github.com/roots/trellis/pull/421))
* Add WP-CLI bash completion script ([#407](https://github.com/roots/trellis/pull/407))
* Add Composer config `github-oauth` variable ([#402](https://github.com/roots/trellis/pull/402))
* Fix copy project local files in example hook ([#404](https://github.com/roots/trellis/pull/404))
* Update cron variable to match Bedrock ([#394](https://github.com/roots/trellis/pull/394))
* Add deploy_build_before example hook for theme assets ([#397](https://github.com/roots/trellis/pull/37))
* Use curl instead of dig for IP lookups ([#390](https://github.com/roots/trellis/pull/390))
* Update SSL cipher suite ([#386](https://github.com/roots/trellis/pull/386))
* Support for other Vagrant providers (VirtualBox, VMWare, Parallels) ([#340](https://github.com/roots/trellis/pull/340))
* Specify versions for Ansible Galaxy requirements ([#385](https://github.com/roots/trellis/pull/385))
* Adds ability to configure [HSTS headers](https://developer.mozilla.org/en-US/docs/Web/Security/HTTP_strict_transport_security) with site variables. ([#388](https://github.com/roots/trellis/pull/388))

### 0.9.2: October 15th, 2015
* Add dev's IP to ferm whitelist ([#381](https://github.com/roots/trellis/pull/381))
* Add nonempty option to config.bindfs.bind_folder ([#382](https://github.com/roots/trellis/pull/382))
* Add proper hooks for task files during deploys ([#378](https://github.com/roots/trellis/pull/378))
* Fix logrotate's Nginx postrotate script ([#377](https://github.com/roots/trellis/pull/377))
* Add static HTML files as fallbacks for Nginx's `index` directive ([#376](https://github.com/roots/trellis/pull/376))
* Use Windows environment variable to determine number of CPUs ([#366](https://github.com/roots/trellis/pull/366))
* Check for galaxy roles before `vagrant up` ([#365](https://github.com/roots/trellis/pull/365))
* Install Xdebug by default in development environment ([#363](https://github.com/roots/trellis/pull/363))
* Ensure admin_user can connect before disabling root ([#345](https://github.com/roots/trellis/pull/345))
* Prevent PHP execution in uploads directory ([#356](https://github.com/roots/trellis/pull/356))
* Update h5bp Nginx configs ([#355](https://github.com/roots/trellis/pull/355))
* Convert sshd role variables to booleans ([#344](https://github.com/roots/trellis/pull/344))
* Add check to validate `subtree_path` during deploy ([#334](https://github.com/roots/trellis/pull/334))
* Rename WP site variable `subtree` to `subtree_path` ([#329](https://github.com/roots/trellis/pull/329))
* Add extra HTTP security headers ([#322](https://github.com/roots/trellis/pull/322))
* HHVM restart cron job fix ([#327](https://github.com/roots/trellis/pull/327))
* Improve SSH remote user detection ([#321](https://github.com/roots/trellis/pull/321))
* Add variable + better default for Nginx fastcgi buffers ([#302](https://github.com/roots/trellis/pull/302))
* WP Multisite install fixes ([#319](https://github.com/roots/trellis/pull/319))
* Re-organize `group_vars` files into subdirectories and separate files ([#308](https://github.com/roots/trellis/pull/308))

### 0.9.1: August 18th, 2015
* Capture development mail with MailHog ([#304](https://github.com/roots/trellis/pull/304))
* Update git remote URL before cloning on deploys ([#299](https://github.com/roots/trellis/pull/299))
* Allow user to set the timezone ([#301](https://github.com/roots/trellis/pull/301))
* Improvements to custom Nginx includes ([#242](https://github.com/roots/trellis/pull/242))
* Fix comment in Vagrantfile: use absolute path for ANSIBLE_PATH ([#292](https://github.com/roots/trellis/pull/292))
* Fix remote user handling for AWS ([#290](https://github.com/roots/trellis/pull/290))

### 0.9.0: August 3rd, 2015
* Allow auto-generation of self signed SSL certificate
* Merge secure-root.yml into server.yml
* Bump Ansible requirement to >= 1.9.2
* Validate that at least the minimum required version of Ansible is used
* Fix PHP error handling
* Flush wp db theme roots on deploy
* Stop recursive copying of vendor
* Update the bin/windows.sh script with absolute path
* Conditionally copy .env into web root
* Add subtree commented out
* Add Composer binary path to the default path
* Change base box to stock Ubuntu 14.04
* Rename bedrock-ansible to Trellis
* Restore strip_www functionality
* Protect against Logjam attack by generating a strong and unique Diffie-Hellman group
* Move SSH key handling to users role
* Fix multisite conditional in wordpress-site.conf
* Allow use of FastCGI caching
* Wrap octal mode in quotes
* Fix project_shared_children mode defaults
* Allow for custom permissions for shared sources
* Provide a mechanism for custom Nginx includes
* Add trailing slash to WP core rewrite, preventing possible redirect loop
* Insert full path to service command, add hhvm restart minute
* Disable exposing PHP version to the world
* wordpress-install improvements
* Nginx h5bp config improvements
* Make composer self-update idempotent
* Fix project_subtree conditional
* Remove redundant site_name when naming log files
* Fix project_subtree check
* Fix conditional check for multi-site deploys
* Fix .env generation for wordpress-install
* Mirror `server_name` in SSL and non-SSL blocks
* Windows compatibility
* Add swapfile role
* Nginx: better worker_processes setting
* Use inventory_hostname instead of ansible_hostname
* Update Ansible version requirements
* Add information on how to deploy with the git strategy
* Define provider as virtualbox to avoid failure
* Don't set HSTS header over HTTP
* Add note about generating keys from the WordPress API
* Use site instead of example.com
* Be consistent with roots-example-project repo
* Add vagrant-hostsupdater to requirements
* SSL support
* Vagrant: resolve site paths relative to Ansible
* Subtree should be defined on a site
* Remove static IP from site_hosts
* Deploy improvements
* WP subdomain multisite support
* Add xdebug role
* Add logrotate role
* Add ntpd role
* Ansible deploys
* HHVM implementation
* Add SMTP role
* Install php5-memcached
* Update to PHP 5.6
* Simplify Vagrantfile
* Add better SSH defaults
* Add fail2ban, ferm for added security
* Remove naming restriction on Bedrock path
* Add vagrant-bindfs for custom NFS permissions
* Limit `sendfile off` directive to development env
* Add better upload size and execution time defaults
* Use H5BP server configs
* Hardcode Vagrant VM memory to 1GB
* Replace dots in cron file names
* Use NFS for shared folders and better performance
* Tagged playbook roles

### 0.4.0: September 9th, 2014
* Complete memcached implementation
* Better PHP production configs: errors and opcache
* Always set fastcgi param `SCRIPT_FILENAME` in Nginx for better version compatibility

### 0.3.0: August 20th, 2014
* Ansible 1.6.8 compatibility (bug fix)
* Fix for slow network connections
* Nginx reload after DB import
* Integrate vagrant-hostsupdater
* Improve organization and file/folder structure
* MySQL password support
* Memcached role
* Improved hosts file and group_vars for separate environments

### 0.2.0: May 15th, 2014
* Add roots/bedrock Vagrant box
* Add `run_composer` option to `wordpress_sites` so Composer can be run on the VM removing the requirement for it on the host
* Remove upgrade role since we can't control package versions with it

### 0.1.1: May 1st, 2014
* Initial release
