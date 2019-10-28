import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_java_installed(host):
    java_version = host.run('java -version')
    assert java_version.rc == 0


def test_bonita_home_dir(host):
    home_folder = host.user().home
    f = host.file(home_folder + '/bonita')
    assert f.exists
