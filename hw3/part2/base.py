import sqlalchemy
from sqlalchemy.orm import sessionmaker


class MyBase:
    '''Create database and establish connection with it'''

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, db, user, password, clean=True):
        self.clean = clean
        self.db = db
        self.user = user
        self.password = password
        self.host = 'localhost'
        self.port = 3306
        self.connection = self.set_connection()
        self.session = sessionmaker(bind=self.connection.engine)()

    # ------------------------------------------------------------------------------------------------------------------
    def get_engine_connect(self, flag=False):
        return sqlalchemy.create_engine(f'mysql+pymysql://{self.user}:{self.password}@'
                                        f'{self.host}:{self.port}/{self.db if flag else ""}', encoding='utf8').connect()

    # ------------------------------------------------------------------------------------------------------------------
    def set_connection(self):
        '''Create connection between db and python'''
        try:
            if self.clean:
                connection = self.get_engine_connect()
                connection.execute(f'DROP DATABASE IF EXISTS {self.db}')
                connection.execute(f'CREATE DATABASE {self.db}')
                connection.close()

            connection = self.get_engine_connect(flag=True)
        except sqlalchemy.exc.InternalError:
            connection = self.get_engine_connect()
            connection.execute(f'CREATE DATABASE {self.db}')
            connection.close()
            connection = self.get_engine_connect(flag=True)
        return connection
