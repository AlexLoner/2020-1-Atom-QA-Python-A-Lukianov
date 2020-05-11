import pytest
import requests

from part2.base import MyBase
from part3 import mock
from part4.remote_cmds import SSH

# ------------------------------------------------------------------------------------------------------------------
@pytest.fixture()
def orm_connect():
    return MyBase(db='test_base', user='loner', password='password')

# ------------------------------------------------------------------------------------------------------------------
@pytest.fixture(scope='session')
def mock_server():
    server = mock.run_mock()
    server_host = server._kwargs['host']
    server_port = server._kwargs['port']

    yield server_host, server_port

    shutdown_url = f'http://{server_host}:{server_port}/shutdown'
    requests.get(shutdown_url)

# ------------------------------------------------------------------------------------------------------------------
@pytest.fixture(scope='session')
def ssh_config():
    ssh_host = '192.168.56.101'
    ssh_port = 2022
    nginx_port = 3000
    name = 'kenny'
    password = 'kenny'

    rise_up_nginx_cmds = [f'semanage port -m -t http_port_t -p tcp {nginx_port}',
                          f'firewall-cmd --add-port={nginx_port}/tcp --permanent',
                           'firewall-cmd --reload',
                           'systemctl restart nginx']

    fall_down_nginx_cmds = [f'firewall-cmd --remove-port={nginx_port}/tcp --permanent',
                             'firewall-cmd --reload',
                             'systemctl restart nginx']

    return {'ssh_host': ssh_host, 'ssh_port': ssh_port, 'name': name, 'password': password,
            'nginx_port': nginx_port, 'rise_up_nginx': rise_up_nginx_cmds, 'fall_down_nginx': fall_down_nginx_cmds}

# ------------------------------------------------------------------------------------------------------------------
@pytest.fixture(scope='session')
def ssh_client(ssh_config):
    with SSH(hostname=ssh_config['ssh_host'], username=ssh_config['name'],
             password=ssh_config['password'], port=ssh_config['ssh_port']) as ssh_server:
        yield ssh_server

