import os
import json
import sys
from main_log_parser import LogBase
from my_errors import PathError


class Log(LogBase):

    # -------------------------------------------------------------------------------------
    def __init__(self, path, json=True):
        self.path = path
        self.json = json

    # -------------------------------------------------------------------------------------
    def make_dict(self, ar, *names):
        d = {}

        if len(ar[0]) == 1:
            for i, item in enumerate(ar):
                d[i] = dict(zip([names[i]], item))
            return d

        for i, item in enumerate(ar):
            d[i] = dict(zip(names, item))
        return d

    # -------------------------------------------------------------------------------------
    def write_logs(self):
        if os.path.isfile(self.path):
            name = self.path.split('/')[-1]
            self._write_log(name, self.path)
        elif os.path.isdir(self.path):
            for file in os.listdir(self.path):
                self._write_log(file, os.path.join(self.path, file))
        else:
            raise PathError()

    # -------------------------------------------------------------------------------------
    def _write_log(self, name, path):
        out_file = f'py_res_{name}'
        with open(out_file, 'w') as f:
            res = self.total_count(path)
            f.write('---------------- TOTAL REQUESTS NUMBER -------------------\n')
            if self.json:
                js1 = self.make_dict([[res]], 'req_number')

            f.write(str(res) + '\n')
            f.write("\n")

            f.write('---------------- REQUESTS NUMBER BY TYPE -----------------\n')
            RES = self.type_count(path)
            if self.json:
                res = [[tmp[1]] for tmp in RES]
                js2 = self.make_dict(res, "GET", "POST", "PUT", "HEAD", "DELETE", "OPTIONS", "CONNECT")

            for res in RES:
                f.write(f'{res[0]}: {res[1]}\n')
            f.write("\n")

            f.write('---------------- TOP 10 REQUESTS SIZE  -----------------\n')
            RES = self.top_10_by_size(path)
            if self.json:
                js3 = self.make_dict(RES, 'req_size', 'count', 'url', 'status_code')

            for res in RES:
                f.write(f'{res[1]} :: {res[0]} :: {res[2]} :: {res[3]}\n')
            f.write("\n")

            f.write('---------------- TOP 10 CLIENT ERROR WITH IP ------------\n')

            RES = self.top_10_client_error_by_number_with_ip(path)
            if self.json:
                js4 = self.make_dict(RES, 'count', 'url', 'status_code', 'ip')

            for res in RES:
                f.write(f'{res[0]} :: {res[1]} :: {res[2]} :: {res[3]}\n')
            f.write("\n")

            f.write('---------------- TOP 10 CLIENT ERROR BY SIZE WITH IP ------------\n')
            RES = self.top_10_client_error_by_size_with_ip(path)
            if self.json:
                js5 = self.make_dict(RES, 'req_size', 'count', 'url', 'status_code', 'ip')

            for res in self.top_10_client_error_by_size_with_ip(path):
                f.write(f'{res[1]} :: {res[0]} :: {res[2]} :: {res[3]} :: {res[4]}\n')
            f.write("\n")

            if self.json:
                d = {
                    'total_requests': js1,
                    'requests_number_by_type': js2,
                    'top_10_by_size': js3,
                    'top_10_client_error_by_number_with_ip': js4,
                    'top_10_client_error_by_size_with_ip': js5
                }
                with open(f'{out_file}_data_json.json', 'w') as f:
                    json.dump(d, f)



if __name__ == "__main__":

    log = Log(sys.argv[1])
    log.write_logs()
