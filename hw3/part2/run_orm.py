import os
from part2.pyglog import LogSQL

from part2.base import MyBase

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../logs/nginx_logs'))
base = MyBase('test_base', user='loner', password='password', clean=True)


log = LogSQL(path=path, data_base=base)
log.fill_database(kind='full_table', lines=10)
log.fill_database(kind='total_logs_table')
log.fill_database(kind='types_logs_table')
log.fill_database(kind='top_10_by_size_table')
log.fill_database(kind='top_10_client_error_by_number_with_ip_table')
log.fill_database(kind='top_10_client_error_by_size_with_ip_table')


