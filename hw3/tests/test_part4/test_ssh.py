import pytest
import requests

# ------------------------------------------------------------------------------------------------------------------
class TestSSH:

    # ------------------------------------------------------------------------------------------------------------------
    @pytest.mark.ssh
    def test_root(self, ssh_client, ssh_config):
        cmd = 'tail -n 10 /var/log/messages'
        ssh_client.root_password = ssh_config['password']
        ssh_client.exec_cmd(cmd=cmd, root=True)

    # ------------------------------------------------------------------------------------------------------------------
    @pytest.mark.ssh
    def test_nginx_conection_http(self, ssh_config):

        res = requests.get(url=f'http://{ssh_config["ssh_host"]}:{ssh_config["nginx_port"]}')
        assert 200 == res.status_code

    # ------------------------------------------------------------------------------------------------------------------
    @pytest.mark.ssh
    def test_nginx_connection_ssh(self, ssh_client, ssh_config):
        ssh_client.root_password = ssh_config['password']
        cmd = 'netstat -tlpn | grep nginx'
        res = ssh_client.exec_cmd(cmd=cmd, root=True)
        assert res.find(':3000') != -1

    # ------------------------------------------------------------------------------------------------------------------
    @pytest.mark.ssh
    def test_access_log(self, ssh_client, ssh_config):
        ssh_client.root_password = ssh_config['password']
        cmd = 'wc -l /var/log/nginx/access.log'
        res1 = ssh_client.exec_cmd(cmd=cmd, root=True).split()[0]
        requests.get(url=f'http://{ssh_config["ssh_host"]}:{ssh_config["nginx_port"]}')
        res2 = ssh_client.exec_cmd(cmd=cmd, root=True).split()[0]
        assert int(res2) > int(res1)

    # ------------------------------------------------------------------------------------------------------------------
    @pytest.mark.ssh
    def test_disable_nginx(self, ssh_client, ssh_config):
        ssh_client.root_password = ssh_config['password']
        for cmd in ssh_config['fall_down_nginx']:
            ssh_client.exec_cmd(cmd=cmd, root=True)
        try:
            requests.get(url=f'http://{ssh_config["ssh_host"]}:{ssh_config["nginx_port"]}')
        except OSError:
            cmd = 'systemctl status nginx'
            res = ssh_client.exec_cmd(cmd=cmd, root=True)
        finally:
            for cmd in ssh_config['rise_up_nginx']:
                ssh_client.exec_cmd(cmd=cmd, root=True)
        assert res.find('Active: active (running)'), res





