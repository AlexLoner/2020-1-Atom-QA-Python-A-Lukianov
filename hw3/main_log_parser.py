import io
from datetime import datetime
from my_errors import InCorrectFileFormat, BrokenFileError, PathError


class LogBase:

    req_types = ["GET", "POST", "PUT", "HEAD", "DELETE", "OPTIONS", "CONNECT"]


    # -------------------------------------------------------------------------------------
    def parse_log(self, line: str):
        line = line.strip()
        spaces = line.split(" ")
        quotes = line.split('"')
        data = {'ip': spaces[0],
                "user": spaces[2],
                "time_local": datetime.strptime(spaces[3][1:], '%d/%b/%Y:%H:%M:%S'),
                'request': quotes[1],
                'status_code': int(spaces[8]),
                'request_size_bytes': float(spaces[9]),
                "http_referer": quotes[-4],
                'user_agent': quotes[-2]
                }
        return data

    # -------------------------------------------------------------------------------------
    def get_log(self, line: str):
        try:
            log = self.parse_log(line)
        except IndexError:
            msg = 'Expected file with next log configuration: $remote_addr - $remote_user [$time_local] ' \
                  '"$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"'
            raise InCorrectFileFormat(msg)
        except io.UnsupportedOperation:
            raise BrokenFileError('Broken File')
        return log

    # -------------------------------------------------------------------------------------
    def total_count(self, path):
        with open(path) as f:
            res = 0
            while f.readline():
                res += 1
        return res

    # -------------------------------------------------------------------------------------
    def type_count(self, path):

        counter = dict(zip(self.req_types, [0 for _ in range(7)]))
        with open(path) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                for req_type in counter:
                    if line.find(req_type) != -1:
                        counter[req_type] += 1
                        continue
        array = []
        for i in self.req_types:
            array.append([i, counter[i]])
        return array

    # -------------------------------------------------------------------------------------
    def top_10_by_size(self, path):
        counter = {}
        with open(path) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                log = self.get_log(line)
                req_size, status_code, url = log['request_size_bytes'], log['status_code'], log['request'].split()[1]
                if (req_size, status_code, url) in counter:
                    counter[(req_size, status_code, url)] += 1
                else:
                    counter.update({(req_size, status_code, url): 1})
        array = []
        for k, v in counter.items():
            array.append([int(k[0]), v, k[2], k[1]])
        array.sort(reverse=True)
        array = array[:10]
        return array

    # -------------------------------------------------------------------------------------
    def top_10_client_error_by_number_with_ip(self, path):
        counter = {}
        with open(path) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                log = self.get_log(line)
                ip, status_code, url = log['ip'], log['status_code'], log['request'].split()[1]
                if 400 <= int(status_code) < 500:
                    if (ip, status_code, url) in counter:
                        counter[(ip, status_code, url)] += 1
                    else:
                        counter.update({(ip, status_code, url): 1})
        array = []
        for k, v in counter.items():
            array.append([v, k[2], k[1], k[0]])
        array.sort(reverse=True)
        return array[:10]

    # -------------------------------------------------------------------------------------
    def top_10_client_error_by_size_with_ip(self, path):
        counter = {}
        with open(path) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                log = self.get_log(line)
                req_size, ip = log['request_size_bytes'], log['ip']
                status_code, url = log['status_code'], log['request'].split()[1]
                if 400 <= int(status_code) < 500:
                    if (req_size, ip, status_code, url) in counter:
                        counter[(req_size, ip, status_code, url)] += 1
                    else:
                        counter.update({(req_size, ip, status_code, url): 1})
        array = []
        for k, v in counter.items():
            array.append([k[0], v, k[3], k[2], k[1]])
        array.sort(reverse=True)
        return array[:10]


