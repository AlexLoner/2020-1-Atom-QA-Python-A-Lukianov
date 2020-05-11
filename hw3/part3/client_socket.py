import socket
import json


host = '127.0.0.1'
port = 5555
params = '/example/5'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.1)

client.connect((host, port))

request = f'GET {params} HTTP/1.1\r\nHost:{host}\r\n\r\n'
client.send(request.encode())

data = []
while True:
    tmp = client.recv(2048)
    if tmp:
        data.append(tmp.decode())
    else:
        break

response = ' '.join(data).splitlines()

result = {'status_code': response[0].split()[1],
          'body': response[-1],
          'headers': response[1:-1]}
print(json.dumps(result))
