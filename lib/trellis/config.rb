# frozen_string_literal: true

require 'vagrant'
require 'yaml'

module Trellis
  class Config
    def initialize(root_path:)
      @root_path = root_path
    end

    def multisite_subdomains?
      @using_multisite_subdomains ||= begin
        sites.any? do |(_name, site)|
          next false unless multisite = site['multisite']
          multisite.fetch('enabled', false) && multisite.fetch('subdomains', false)
        end
      end
    end

    def site_hosts_canonical
      @site_hosts_canonical ||= site_hosts.map { |host| host['canonical'] }
    end

    def site_hosts_redirects
      @site_hosts_redirects ||= site_hosts.flat_map { |host| host['redirects'] }.compact
    end

    def site_hosts
      @site_hosts ||= begin
        sites.flat_map { |(_name, site)| site['site_hosts'] }.tap do |hosts|
          fail_with message: template_content if malformed?(site_hosts: hosts)
        end
      end
    end

    def sites
      @sites ||= begin
        content['sites'].tap do |sites|
          fail_with message: "No sites found in #{path}." if sites.to_h.empty?
        end
      end
    end

    def content
      @content ||= begin
        fail_with message: "#{path} was not found. Please check `root_path`." unless exist?
        YAML.load_file(path)
      end
    end

    private

    def malformed?(site_hosts:)
      site_hosts.any? do |host|
        !host.is_a?(Hash) || !host.key?('canonical')
      end
    end

    def exist?
      File.exist?(path)
    end

    def path
      File.join(@root_path, 'group_vars', 'development', 'sites.yml')
    end

    def template_content
      File.read(File.join(@root_path, 'roles', 'common', 'templates', 'site_hosts.j2')).sub!('{{ env }}', 'development').gsub!(/com$/, 'dev')
    end

    def fail_with(message:)
      raise Vagrant::Errors::VagrantError.new, message
    end
  end
end
