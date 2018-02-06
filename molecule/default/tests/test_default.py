import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE'],
).get_hosts('all')


def test_inspector_files(host):
    vars = host.ansible(
        'include_vars',
        'file=../../defaults/main.yml',
    ).get('ansible_facts')

    agent_dest = vars.get('sansible_amazon_inspector_agent_dest')

    installer = host.file(agent_dest)
    assert installer.exists
    assert installer.user == 'root'
    assert installer.group == 'root'
    assert installer.mode == 493  # 0755 oct

    sig = host.file(agent_dest + '.sig')
    assert sig.exists
    assert sig.user == 'root'
    assert sig.group == 'root'
    assert sig.mode == 420  # 0644 oct

    key = host.file(agent_dest + '.key')
    assert key.exists
    assert key.user == 'root'
    assert key.group == 'root'
    assert key.mode == 420  # 0644 oct
