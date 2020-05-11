from part2.base import MyBase
from part2.entity import Base


class Table:

    # ---------------------------------------------------------------------------------------------
    def __init__(self, base: MyBase, entity):
        self.base = base
        self.engine = self.base.connection.engine
        self.create_table(entity.__tablename__)

    # ---------------------------------------------------------------------------------------------
    def create_table(self, name):
        if not self.engine.dialect.has_table(self.engine, name):
            Base.metadata.tables[name].create(self.engine)

    # ---------------------------------------------------------------------------------------------
    def create(self, entity):
        self.base.session.add(entity)
        self.base.session.commit()

    # ------------------------------------------------------------------------------------------------------------------
    def all(self, entity):
        '''Return all items for table'''
        return self.base.session.query(entity).all()
