# Set Ansible paths relative to Ansible directory
ENV['ANSIBLE_CONFIG'] = ANSIBLE_PATH
ENV['ANSIBLE_CALLBACK_PLUGINS'] = "~/.ansible/plugins/callback:/usr/share/ansible/plugins/callback:#{File.join(ANSIBLE_PATH, 'lib/trellis/plugins/callback')}"
ENV['ANSIBLE_FILTER_PLUGINS'] = "~/.ansible/plugins/filter:/usr/share/ansible/plugins/filter:#{File.join(ANSIBLE_PATH, 'lib/trellis/plugins/filter')}"
ENV['ANSIBLE_LIBRARY'] = "~/.ansible/plugins/modules:/usr/share/ansible/plugins/modules:#{File.join(ANSIBLE_PATH, 'lib/trellis/modules')}"
ENV['ANSIBLE_ROLES_PATH'] = File.join(ANSIBLE_PATH, 'vendor', 'roles')
ENV['ANSIBLE_VARS_PLUGINS'] = "~/.ansible/plugins/vars:/usr/share/ansible/plugins/vars:#{File.join(ANSIBLE_PATH, 'lib/trellis/plugins/vars')}"

def ensure_plugins(plugins)
  logger = Vagrant::UI::Colored.new
  installed = false

  plugins.each do |plugin|
    plugin_name = plugin['name']
    manager = Vagrant::Plugin::Manager.instance

    next if manager.installed_plugins.has_key?(plugin_name)

    logger.warn("Installing plugin #{plugin_name}")

    manager.install_plugin(
      plugin_name,
      sources: plugin.fetch('source', %w(https://rubygems.org/ https://gems.hashicorp.com/)),
      version: plugin['version']
    )

    installed = true
  end

  if installed
    logger.warn('`vagrant up` must be re-run now that plugins are installed')
    exit
  end
end

def fail_with_message(msg)
  fail Vagrant::Errors::VagrantError.new, msg
end

def local_provisioning?
  @local_provisioning ||= Vagrant::Util::Platform.windows? || !which('ansible-playbook') || ENV['FORCE_ANSIBLE_LOCAL']
end

def local_site_path(site)
  File.expand_path(site['local_path'], ANSIBLE_PATH)
end

def nfs_path(path)
  "/vagrant-nfs-#{File.basename(path)}"
end

def mount_options(mount_type, dmode:, fmode:)
  if mount_type == 'smb'
    ["vers=3.02", "mfsymlinks", "dir_mode=0#{dmode}", "file_mode=0#{fmode}", "sec=ntlm"]
  else
    ["dmode=#{dmode}", "fmode=#{fmode}"]
  end
end

def post_up_message
  msg = 'Your Trellis Vagrant box is ready to use!'
  msg << "\n* Composer and WP-CLI commands need to be run on the virtual machine"
  msg << "\n  for any post-provision modifications."
  msg << "\n* You can SSH into the machine with `vagrant ssh`."
  msg << "\n* Then navigate to your sites at `/srv/www`"
  msg << "\n  or to your Trellis files at `#{ANSIBLE_PATH_ON_VM}`."

  msg
end

def remote_site_path(site_name, site)
  "/srv/www/#{site_name}/#{site['current_path'] || 'current'}"
end

def which(cmd)
  exts = ENV['PATHEXT'] ? ENV['PATHEXT'].split(';') : ['']

  paths = ENV['PATH'].split(File::PATH_SEPARATOR).flat_map do |path|
    exts.map { |ext| File.join(path, "#{cmd}#{ext}") }
  end

  paths.any? do |path|
    next unless File.executable?(path) && !File.directory?(path)
    system("#{path} --help", %i(out err) => File::NULL)
  end
end

def update_ssh_config(main_hostname)
  regexp = /(Host #{Regexp.quote(main_hostname)}(?:(?!^Host).)*)/m
  config_file = File.expand_path('~/.ssh/config')
  vagrant_ssh_config = `vagrant ssh-config --host #{main_hostname}`.chomp

  if File.exists?(config_file)
    FileUtils.cp(config_file, "#{config_file}.trellis_backup")
    ssh_config = File.read(config_file)

    content = if ssh_config =~ regexp
      ssh_config.gsub(regexp, vagrant_ssh_config)
    else
      ssh_config << "\n#{vagrant_ssh_config}"
    end

    File.write(config_file, content)
  else
    File.write(config_file, vagrant_ssh_config)
  end
end
