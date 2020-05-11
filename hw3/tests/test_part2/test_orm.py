import pytest
import os

from part2.entity import TotalLog
from part2.pyglog import LogSQL


@pytest.mark.orm
def test_create(orm_connect):

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logs/nginx_logs'))
    logging = LogSQL(path=path, data_base=orm_connect)
    logging.fill_database(kind='total_logs_table')
    assert len(logging.table.all(TotalLog)) == 1
