import io
import os
from datetime import datetime

from main_log_parser import LogBase
from my_errors import InCorrectFileFormat, BrokenFileError, PathError
from part2.base import MyBase
from part2.table import Table
from part2.entity import FullLog, TotalLog, TypeLog, Top10BySize, Top10ClientErrorIP, Top10ClientErrorSize


class LogSQL(LogBase):

    # -------------------------------------------------------------------------------------
    def __init__(self, path, data_base: MyBase):
        self.path = path
        self.base = data_base

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
    def fill_database(self, kind, lines=None):
        '''
        Filling table by type kind
        kind : <string> :: ['full_table', 'total_logs_table', 'types_logs_table', 'top_10_by_size_table',
                            'top_10_client_error_by_number_with_ip_table', 'top_10_client_error_by_size_with_ip_table']
        '''
        method = getattr(self, kind)
        if os.path.isfile(self.path):
            if kind == 'full_table':
                method(self.path, lines=lines)
            else:
                method(self.path)
        elif os.path.isdir(self.path):
            for file in os.listdir(self.path):
                if kind == 'full_table':
                    method(os.path.join(self.path, file), lines=lines)
                else:
                    method(os.path.join(self.path, file))
        else:
            raise PathError(f"{self.path} not a directory either file")

    # -------------------------------------------------------------------------------------
    def full_table(self, file, lines):
        '''Convert all logs from file to database with name '''
        self.table = Table(self.base, FullLog)
        flag = True
        with open(file, 'r') as f:
            c = 0
            while True and flag:
                line = f.readline()
                if not line:
                    break
                log = self.get_log(line)
                self.table.create(entity=FullLog(**log))
                c += 1
                if lines:
                    if c >= lines:
                        flag = False

    # -------------------------------------------------------------------------------------
    def total_logs_table(self, file):
        self.table = Table(self.base, TotalLog)
        res = self.total_count(file)
        self.table.create(entity=TotalLog(res))

    # -------------------------------------------------------------------------------------
    def types_logs_table(self, file):
        self.table = Table(self.base, TypeLog)
        res = self.type_count(file)
        self.table.create(entity=TypeLog(**dict(res)))

    # -------------------------------------------------------------------------------------
    def top_10_by_size_table(self, file):
        self.table = Table(self.base, Top10BySize)
        res = self.top_10_by_size(file)
        keys = ['request_size_bytes', 'times', 'url', 'status_code']
        for r in res:
            self.table.create(entity=Top10BySize(**dict(zip(keys, r))))

    # -------------------------------------------------------------------------------------
    def top_10_client_error_by_number_with_ip_table(self, file):
        self.table = Table(self.base, Top10ClientErrorIP)
        res = self.top_10_client_error_by_number_with_ip(file)
        keys = ['times', 'url', 'status_code', 'ip']
        for r in res:
            self.table.create(entity=Top10ClientErrorIP(**dict(zip(keys, r))))

    # -------------------------------------------------------------------------------------
    def top_10_client_error_by_size_with_ip_table(self, file):
        self.table = Table(self.base, Top10ClientErrorSize)
        res = self.top_10_client_error_by_size_with_ip(file)
        keys = ['times', 'request_size_bytes', 'url', 'status_code', 'ip']
        for r in res:
            self.table.create(entity=Top10ClientErrorSize(**dict(zip(keys, r))))


