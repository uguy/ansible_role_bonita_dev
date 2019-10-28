bonita_dev
==========

[![License](https://img.shields.io/github/license/uguy/ansible_role_bonita_dev?style=plastic)](https://raw.githubusercontent.com/uguy/ansible-role-bonita_dev/master/LICENSE)
[![Build Status](https://travis-ci.org/uguy/ansible_role_bonita_dev.svg?branch=master)](https://travis-ci.org/uguy/ansible_role_bonita_dev)

[![Platform](http://img.shields.io/badge/platform-ubuntu-dd4814.svg?style=plastic)](Ubuntu)

An [Ansible](http://www.ansible.com) role to setup Bonita Community server on a developer box.

Requirements
------------

- ansible >= 2.x

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

### Debian/Ubuntu

- **bonita_bundle**: "BonitaCommunity-{{ bonita_version }}-tomcat.zip"
- **bonita_home_dir**: "~/bonita"
- **bonita_install_dir**: "{{ bonita_home_dir }}/BonitaCommunity-{{ bonita_version }}-tomcat"
- **bonita_required_packages**:  ['unzip']
- **bonita_java_package**:  'openjdk-11-jre-headless'

Playbooks
---------

```yaml
    - hosts: localhost
      roles:
         - { role: bonita_dev }
```

Tests
-----

```bash
molecule test
```

| Family | Distribution | Version | Test Status |
|:-:|:-:|:-:|:-:|
| Debian | Ubuntu  | Bionic    | [![x86_64](http://img.shields.io/badge/x86_64-passed-006400.svg?style=flat)](x) |

License
-------

GPLv3

Links
-----

- [Bonitasoft](https://documentation.bonitasoft.com/bonita/current/_getting-started-tutorial)
- [Ansible](http://www.ansible.com)
- [Molecule](https://molecule.readthedocs.io/en/stable/)