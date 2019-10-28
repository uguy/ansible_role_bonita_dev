![bonitasoft](https://community.bonitasoft.com/sites/community/files/logo_community_0.png) 

bonita_dev
==========

[![License](https://img.shields.io/github/license/uguy/ansible_role_bonita_dev?style=plastic)](https://raw.githubusercontent.com/uguy/ansible_role_bonita_dev/master/LICENSE)
[![Build Status](https://api.travis-ci.com/uguy/ansible_role_bonita_dev.svg?branch=master)](https://travis-ci.com/uguy/ansible_role_bonita_dev)

An [Ansible](http://www.ansible.com) role to setup [Bonita Community server](https://fr.bonitasoft.com/telechargez) on a developer box.

Bonita server is installed in the user's home directory as default. A new tenant password is randomly generated on each run and the user is notified by an email providing the new tenant password.

> This purpose of this repo is to play with ansible, molecule and Bonita BPM community server, thus not for production use :innocent:

Requirements
------------

- ansible >= 2.x
- Requires at least Java 8. See [`geerlingguy.java`](https://github.com/geerlingguy/ansible-role-java#example-playbook-install-openjdk-8) role instructions for installing OpenJDK 8.

Facts
-----

- **java_installed**: fact set by this role that contains a flag that indicates if Java is installed on the host.
- **java_version_installed**: fact set by this role that contains the string of the Java version installed in the system.
- **tenant_admin_password**: fact set by this role that contains the string of the randomly generated password for the tenant user `Install` (generated each run).

Role Variables
--------------

- **debug**: flag to make role more verbose.
- **bonita_version**: 7.9.4
- **bonita_repo_url**: "https://release.ow2.org/bonita"
- **smtp.host**: "my.smtp.host.com"
- **smtp.port**: 2525
- **smtp.username**: smtp_user
- **smtp.password**: 123456789
- **smtp.from**: "bonita-admin@my.smtp.host.com"
- **smtp.to**: "bonita-user@somewhere.com"
- **smtp.TLS**: starttls

### Debian/Ubuntu

- **bonita_home_dir**: "~/bonita"
- **bonita_required_packages**:  ['unzip']

Playbooks
---------

```yaml
    - hosts: localhost
      roles:
         - role: bonita_dev
           vars:
              smtp.to: "bonita-user@somewhere.com"
```

Tests
-----

```bash
molecule test
```

| Family | Distribution | Version | Test Status |
|:-:|:-:|:-:|:-:|
| Debian | Ubuntu  | Bionic    | [![x86_64](http://img.shields.io/badge/x86_64-passed-006400.svg?style=flat)](x) |
| Debian | Ubuntu  | Xenial    | [![x86_64](http://img.shields.io/badge/x86_64-passed-006400.svg?style=flat)](x) |
| Debian | Debian  | Buster    | [![x86_64](http://img.shields.io/badge/x86_64-passed-006400.svg?style=flat)](x) |
| Debian | Debian  | Stretch   | [![x86_64](http://img.shields.io/badge/x86_64-passed-006400.svg?style=flat)](x) |

License
-------

GPLv3

Links
-----

- [Bonitasoft](https://documentation.bonitasoft.com/bonita/current/_getting-started-tutorial)
- [Ansible](http://www.ansible.com)
- [Molecule](https://molecule.readthedocs.io/en/stable/)
