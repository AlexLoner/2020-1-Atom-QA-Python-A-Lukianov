Делал на CentOs8

ip: 192.168.56.101

Создание ssh сервера: 
1) Добавить строку Port 2022 в /etc/ssh/sshd_config
2) semanage port -a -t ssh_port -p tcp 2022
3) firewall-cmd --add-port 2022/tcp --permanent
4) firewall-cmd --reload

Создание nginx сервера:
0) В файле /etc/nginx/nginx.conf ставить {nginx_port} после listen
1) semanage port -m -t http_port_t -p tcp {nginx_port}
2) firewall-cmd --add-port={nginx_port}/tcp --permanent'
3) firewall-cmd --reload
4) systemctl restart nginx
