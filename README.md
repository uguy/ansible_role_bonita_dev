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

Role Variables
--------------

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