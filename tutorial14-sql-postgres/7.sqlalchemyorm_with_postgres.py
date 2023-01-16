from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://akrocky:akrocky01@localhost/company_sales")
Base = declarative_base(engine)
Base.metadata.reflect(engine)


class Sale(Base):
    __table__ = Base.metadata.tables['sale']

    def __repr__(self):
        return '''<Sale(order_num='{0}',order_type={1},cust_name='{2}',prod_name='{3}',quantity='{4}',order_total='{5}','''.format(self.order_num,
                                                                                                                                   self.order_type, self.cust_name, self.prod_name, self.quantity, self.order_total)


def load_session():
    session = sessionmaker(bind=engine)
    session = session()
    return session


if __name__ == "__main__":
    session = load_session()
    # Read
    smallest_sale = session.query(Sale).limit(3).all()
    print(smallest_sale)
    # print(smallest_sale[0].cust_name)
    # # insert
    # insert_sale = Sale(order_num=11112138,
    #                    order_type='Retail', cust_name="Ak Rocky",
    #                    prod_number="MH111", prod_name="HTML-CSS Bootcamp", quantity=15, price=10, discount=0, order_total=3375)
    # print(insert_sale)
    # session.add(insert_sale)
    # session.commit()
    # # Update
    # insert_sale.quantity = 4
    # insert_sale.order_total = 30000
    # session.commit()
    # updated_sale = session.query(Sale).filter(
    #     Sale.order_num == 11112138).first()
    # print("updated",updated_sale)
    # # detele
    # returned_sale = session.query(Sale).filter(
    #     Sale.order_num == 11112138).first()
    # session.delete(returned_sale)
    # session.commit()
