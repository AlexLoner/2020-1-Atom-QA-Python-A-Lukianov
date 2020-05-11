from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# -------------------------------------------------------------------------------------
class FullLog(Base):

    __tablename__ = 'full_log_base'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(100), nullable=False)
    user = Column(String(100))
    time_local = Column(DateTime, nullable=False)
    request = Column(String(250), nullable=False)
    status_code = Column(Integer, nullable=False)
    request_size_bytes = Column(Float, nullable=False)
    http_referer = Column(String(250))
    user_agent = Column(String(250))

    # -------------------------------------------------------------------------------------
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, kwargs[k])

    # -------------------------------------------------------------------------------------
    def __repr__(self):
        s = f"{self.ip} :: {self.user} :: {self.time_local} :: {self.request} ::" \
            f" {self.status_code} :: {self.request_size_bytes} :: {self.http_referer} :: {self.user_agent}"
        return s


# ------------------------------------------------------------------------------------
class TotalLog(Base):

    __tablename__ = 'total_logs'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_logs_number = Column(Integer, nullable=False)

    # -------------------------------------------------------------------------------------
    def __init__(self, total):
        self.total_logs_number = total


# -------------------------------------------------------------------------------------
class TypeLog(Base):

    __tablename__ = 'types_logs'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    GET = Column(Integer, nullable=False)
    POST = Column(Integer, nullable=False)
    PUT = Column(Integer, nullable=False)
    HEAD = Column(Integer, nullable=False)
    DELETE = Column(Integer, nullable=False)
    OPTIONS = Column(Integer, nullable=False)
    CONNECT = Column(Integer, nullable=False)

    # -------------------------------------------------------------------------------------
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, kwargs[k])


# -------------------------------------------------------------------------------------
class Top10BySize(Base):

    __tablename__ = 'top_10_by_size'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    status_code = Column(Integer, nullable=False)
    request_size_bytes = Column(Float, nullable=False)
    url = Column(String(255), nullable=False)
    times = Column(Integer, nullable=False)

    # -------------------------------------------------------------------------------------
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, kwargs[k])


# -------------------------------------------------------------------------------------
class Top10ClientErrorIP(Base):

    __tablename__ = 'top_10_client_error_by_number_with_ip'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(100), nullable=False)
    status_code = Column(Integer, nullable=False)
    url = Column(String(255), nullable=False)
    times = Column(Integer, nullable=False)

    # -------------------------------------------------------------------------------------
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, kwargs[k])


# -------------------------------------------------------------------------------------
class Top10ClientErrorSize(Base):

    __tablename__ = 'top_10_client_error_by_size_with_ip'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(100), nullable=False)
    request_size_bytes = Column(Float, nullable=False)
    status_code = Column(Integer, nullable=False)
    url = Column(String(255), nullable=False)
    times = Column(Integer, nullable=False)

    # -------------------------------------------------------------------------------------
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, kwargs[k])
