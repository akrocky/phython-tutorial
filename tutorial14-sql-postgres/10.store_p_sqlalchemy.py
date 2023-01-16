from sqlalchemy import MetaData, Table, create_engine

engine = create_engine(
    "postgresql://akrocky:akrocky01@localhost/company_sales")

with engine.connect() as connection:
    meta = MetaData(engine)
    sale_table = Table('sale', meta, autoload=True, autoLoad_with=engine)

    connection.execute('COMMIT')
    connection.execute("CALL return_nondiscounted_item(%s,%s)", (1105910, 2))
