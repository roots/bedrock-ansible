ANSIBLE_PATH = __dir__ # absolute path to Ansible directory on host machine
ANSIBLE_PATH_ON_VM = '/home/vagrant/trellis'.freeze # absolute path to Ansible directory on virtual machine

require File.join(ANSIBLE_PATH, 'lib', 'trellis', 'vagrant')
require File.join(ANSIBLE_PATH, 'lib', 'trellis', 'config')
require 'yaml'

vconfig = YAML.load_file("#{ANSIBLE_PATH}/vagrant.default.yml")

if File.exist?("#{ANSIBLE_PATH}/vagrant.local.yml")
  local_config = YAML.load_file("#{ANSIBLE_PATH}/vagrant.local.yml")
  vconfig.merge!(local_config) if local_config
end

ensure_plugins(vconfig.fetch('vagrant_plugins')) if vconfig.fetch('vagrant_install_plugins')

trellis_config = Trellis::Config.new(root_path: ANSIBLE_PATH)

Vagrant.require_version '>= 2.1.0'

Vagrant.configure('2') do |config|
  config.vm.box = vconfig.fetch('vagrant_box')
  config.vm.box_version = vconfig.fetch('vagrant_box_version')
  config.ssh.forward_agent = true
  config.vm.post_up_message = post_up_message

  # Fix for: "stdin: is not a tty"
  # https://github.com/mitchellh/vagrant/issues/1673#issuecomment-28288042
  config.ssh.shell = %(bash -c 'BASH_ENV=/etc/profile exec bash')

  # Required for NFS to work
  if vconfig.fetch('vagrant_ip') == 'dhcp'
    config.vm.network :private_network, type: 'dhcp', hostsupdater: 'skip'

    cached_addresses = {}
    config.hostmanager.ip_resolver = proc do |vm|
      if cached_addresses[vm.name].nil?
        if vm.communicate.ready?
          vm.communicate.execute("hostname -I | cut -d ' ' -f 2") do |_type, contents|
            cached_addresses[vm.name] = contents.split("\n").first[/(\d+\.\d+\.\d+\.\d+)/, 1]
          end
        end
      end
      cached_addresses[vm.name]
    end
  else
    config.vm.network :private_network, ip: vconfig.fetch('vagrant_ip'), hostsupdater: 'skip'
  end

  main_hostname, *hostnames = trellis_config.site_hosts_canonical
  config.vm.hostname = main_hostname

  if Vagrant.has_plugin?('vagrant-hostmanager') && !trellis_config.multisite_subdomains?
    redirects = trellis_config.site_hosts_redirects

    config.hostmanager.enabled = true
    config.hostmanager.manage_host = true
    config.hostmanager.aliases = hostnames + redirects
  elsif Vagrant.has_plugin?('landrush') && trellis_config.multisite_subdomains?
    config.landrush.enabled = true
    config.landrush.tld = trellis_config.site_hosts_canonical.reject { |host| host.end_with?(".#{main_hostname}") }
    hostnames.each { |host| config.landrush.host host, vconfig.fetch('vagrant_ip') }
  else
    fail_with_message "vagrant-hostmanager missing, please install the plugin with this command:\nvagrant plugin install vagrant-hostmanager\n\nOr install landrush for multisite subdomains:\nvagrant plugin install landrush"
  end

  bin_path = File.join(ANSIBLE_PATH_ON_VM, 'bin')

  vagrant_mount_type = vconfig.fetch('vagrant_mount_type')

  extra_options = if vagrant_mount_type == 'smb'
    {
      smb_username: vconfig.fetch('vagrant_smb_username', 'vagrant'),
      smb_password: vconfig.fetch('vagrant_smb_password', 'vagrant'),
    }
  else
    {}
  end

  if vagrant_mount_type != 'nfs' || Vagrant::Util::Platform.wsl? || (Vagrant::Util::Platform.windows? && !Vagrant.has_plugin?('vagrant-winnfsd'))
    vagrant_mount_type = nil if vagrant_mount_type == 'nfs'
    trellis_config.sites.each_pair do |name, site|
      config.vm.synced_folder local_site_path(site), remote_site_path(name, site), owner: 'vagrant', group: 'www-data', mount_options: mount_options(vagrant_mount_type, dmode: 776, fmode: 775), type: vagrant_mount_type, **extra_options
    end

    config.vm.synced_folder ANSIBLE_PATH, ANSIBLE_PATH_ON_VM, mount_options: mount_options(vagrant_mount_type, dmode: 755, fmode: 644), type: vagrant_mount_type, **extra_options
    config.vm.synced_folder File.join(ANSIBLE_PATH, 'bin'), bin_path, mount_options: mount_options(vagrant_mount_type, dmode: 755, fmode: 755), type: vagrant_mount_type, **extra_options
  elsif !Vagrant.has_plugin?('vagrant-bindfs')
    fail_with_message "vagrant-bindfs missing, please install the plugin with this command:\nvagrant plugin install vagrant-bindfs"
  else
    trellis_config.sites.each_pair do |name, site|
      config.vm.synced_folder local_site_path(site), nfs_path(name), type: 'nfs'
      config.bindfs.bind_folder nfs_path(name), remote_site_path(name, site), u: 'vagrant', g: 'www-data', o: 'nonempty'
    end

    config.vm.synced_folder ANSIBLE_PATH, '/ansible-nfs', type: 'nfs'
    config.bindfs.bind_folder '/ansible-nfs', ANSIBLE_PATH_ON_VM, o: 'nonempty', p: '0644,a+D'
    config.bindfs.bind_folder bin_path, bin_path, perms: '0755'
  end

  vconfig.fetch('vagrant_synced_folders', []).each do |folder|
    options = {
      type: folder.fetch('type', 'nfs'),
      create: folder.fetch('create', false),
      mount_options: folder.fetch('mount_options', [])
    }

    destination_folder = folder.fetch('bindfs', true) ? nfs_path(folder['destination']) : folder['destination']

    config.vm.synced_folder folder['local_path'], destination_folder, options

    if folder.fetch('bindfs', true)
      config.bindfs.bind_folder destination_folder, folder['destination'], folder.fetch('bindfs_options', {})
    end
  end

  provisioner = local_provisioning? ? :ansible_local : :ansible
  provisioning_path = local_provisioning? ? ANSIBLE_PATH_ON_VM : ANSIBLE_PATH

  # Fix for https://github.com/hashicorp/vagrant/issues/10914
  if local_provisioning?
    config.vm.provision 'shell', inline: <<~SHELL
      sudo apt-get update -y -qq &&
      sudo dpkg-reconfigure libc6 &&
      export DEBIAN_FRONTEND=noninteractive &&
      sudo -E apt-get -q --option \"Dpkg::Options::=--force-confold\" --assume-yes install libssl1.1
    SHELL
  end

  config.vm.provision provisioner do |ansible|
    if local_provisioning?
      ansible.install_mode = 'pip'
      if Vagrant::VERSION >= '2.2.5'
        # Fix for https://github.com/hashicorp/vagrant/issues/10950
        ansible.pip_install_cmd = 'curl https://bootstrap.pypa.io/get-pip.py | sudo python'
      end
      ansible.provisioning_path = provisioning_path
      ansible.version = vconfig.fetch('vagrant_ansible_version')
    end

    ansible.compatibility_mode = '2.0'
    ansible.playbook = File.join(provisioning_path, 'dev.yml')
    ansible.galaxy_role_file = File.join(provisioning_path, 'galaxy.yml') unless vconfig.fetch('vagrant_skip_galaxy') || ENV['SKIP_GALAXY']
    ansible.galaxy_roles_path = File.join(provisioning_path, 'vendor/roles')

    ansible.groups = {
      'web' => ['default'],
      'development' => ['default']
    }

    ansible.tags = ENV['ANSIBLE_TAGS']
    ansible.extra_vars = { 'vagrant_version' => Vagrant::VERSION }

    if (vars = ENV['ANSIBLE_VARS'])
      extra_vars = Hash[vars.split(',').map { |pair| pair.split('=') }]
      ansible.extra_vars.merge!(extra_vars)
    end

    if !Vagrant::Util::Platform.windows?
      config.trigger.after :up do |trigger|
        # Add Vagrant ssh-config to ~/.ssh/config
        trigger.info = "Adding vagrant ssh-config for #{main_hostname } to ~/.ssh/config"
        trigger.ruby do
          update_ssh_config(main_hostname)
        end
      end
    end
  end

  # VirtualBox settings
  config.vm.provider 'virtualbox' do |vb|
    vb.name = config.vm.hostname
    vb.customize ['modifyvm', :id, '--cpus', vconfig.fetch('vagrant_cpus')]
    vb.customize ['modifyvm', :id, '--memory', vconfig.fetch('vagrant_memory')]
    vb.customize ['modifyvm', :id, '--ioapic', vconfig.fetch('vagrant_ioapic', 'on')]

    # Fix for slow external network connections
    vb.customize ['modifyvm', :id, '--natdnshostresolver1', vconfig.fetch('vagrant_natdnshostresolver', 'on')]
    vb.customize ['modifyvm', :id, '--natdnsproxy1', vconfig.fetch('vagrant_natdnsproxy', 'on')]
  end

  # VMware Workstation/Fusion settings
  %w(vmware_fusion vmware_workstation).each do |provider|
    config.vm.provider provider do |vmw|
      vmw.vmx['displayName'] = config.vm.hostname
      vmw.vmx['numvcpus'] = vconfig.fetch('vagrant_cpus')
      vmw.vmx['memsize'] = vconfig.fetch('vagrant_memory')
    end
  end

  # Parallels settings
  config.vm.provider 'parallels' do |prl|
    prl.name = config.vm.hostname
    prl.cpus = vconfig.fetch('vagrant_cpus')
    prl.memory = vconfig.fetch('vagrant_memory')
    prl.update_guest_tools = true
  end

  # Hyper-V settings
  config.vm.provider 'hyperv' do |h|
    h.vmname = config.vm.hostname
    h.cpus = vconfig.fetch('vagrant_cpus')
    h.memory = vconfig.fetch('vagrant_memory')
    h.enable_virtualization_extensions = true
    h.linked_clone = true
  end
end
