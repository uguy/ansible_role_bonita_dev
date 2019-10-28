import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_bonita_home_dir(host):
    f = host.file('~/bonita')
    assert f.exists


def test_java_installed(host):
    java_version = host.run('java -version')
    assert java_version.rc == 0
