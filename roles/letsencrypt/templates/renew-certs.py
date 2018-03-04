#!/usr/bin/env python

import os
import sys
import time

from subprocess import CalledProcessError, check_output, STDOUT

failed = False
letsencrypt_cert_ids = {{ letsencrypt_cert_ids }}

for site in {{ apps_using_letsencrypt }}:
    cert_path = os.path.join('{{ letsencrypt_certs_dir }}', site + '-' + letsencrypt_cert_ids[site] + '.cert')
    bundled_cert_path = os.path.join('{{ letsencrypt_certs_dir }}', site + '-' + letsencrypt_cert_ids[site] + '-bundled.cert')

    if os.access(cert_path, os.F_OK):
        stat = os.stat(cert_path)
        print 'Certificate file ' + cert_path + ' already exists'

        if time.time() - stat.st_mtime < {{ letsencrypt_min_renewal_age }} * 86400:
            print '  The certificate is younger than {{ letsencrypt_min_renewal_age }} days. Not creating a new certificate.\n'
            continue

    print 'Generating certificate for ' + site

    cmd = ('/usr/bin/env python {{ acme_tiny_software_directory }}/acme_tiny.py '
           '--quiet '
           '--ca {{ letsencrypt_ca }} '
           '--account-key {{ letsencrypt_account_key }} '
           '--csr {{ acme_tiny_data_directory }}/csrs/{0}-{1}.csr '
           '--acme-dir {{ acme_tiny_challenges_directory }}'
           ).format(site, letsencrypt_cert_ids[site])

    try:
        cert = check_output(cmd, stderr=STDOUT, shell=True)
    except CalledProcessError as e:
        failed = True
        print 'Error while generating certificate for ' + site
        print e.output
    else:
        with open(cert_path, 'w') as cert_file:
            cert_file.write(cert)

        with open('{{ letsencrypt_intermediate_cert_path }}') as intermediate_cert_file:
            intermediate_cert = intermediate_cert_file.read()

        with open(bundled_cert_path, 'w') as bundled_file:
            bundled_file.write(''.join([cert, intermediate_cert]))

        print 'Created certificate for ' + site

if failed:
    sys.exit(1)
