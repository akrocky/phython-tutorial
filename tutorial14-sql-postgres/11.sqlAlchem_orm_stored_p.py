from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://akrocky:akrocky01@localhost/company_sales")
Base = declarative_base(engine)
Base.metadata.reflect(engine)


class Sale(Base):
    _table_ = Base.metadata.tables['sale']

    def __repr__(self):
        return '''<Sale(order_num='{0}',order_type={1},cust_name='{2}',prod_name='{3}',quantity='{4}',order_total='{5}','''.format(self.order_num, self.order_type, self.cust_name, self.prod_name, self.quantity, self.order_total)


if __name__ == "__main__":
    with engine.connect() as connection:
        connection.execute("COMMIT")
        connection.execute(
            "CALL return_nondiscounted_item(%s,%s)", (1105910, 5))
