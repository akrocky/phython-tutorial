from sqlalchemy import Column, MetaData, String, Table, create_engine

engine = create_engine(
    "postgresql://akrocky:akrocky01@localhost/company_sales")
with engine.connect() as connection:
    meta = MetaData(engine)
    sale_table = Table('sale', meta, autoload=True, autoLoad_with=engine)
    adding_record = sale_table.insert().values(order_num=11112136,
                                               order_type='Retail', cust_name="Ak Rocky",
                                               prod_number="MH111", prod_name="HTML-CSS Bootcamp", quantity=15, price=10, discount=0, order_total=150)
    connection.execute(adding_record)
    # reading
    select_statement = sale_table.select().limit(10)
    reselt_set = connection.execute(select_statement)
    for result in reselt_set:
        print("Reading", result)
    # updating
    update_statement = sale_table.update().where(
        sale_table.c.order_num == 11112136).values(quantity=2, order_total=20)
    connection.execute(update_statement)
    # confirming update
    reselect_statement = sale_table.select().where(
        sale_table.c.order_num == 11112136)
    updated_set = connection.execute(reselect_statement)
    for result in updated_set:
        print("updated", result)

    # deleting
    delete_statement = sale_table.delete().where(sale_table.c.order_num == 11112136
                                                 )
    # confirming delete
    note_found_set = connection.execute(reselect_statement)
    print("Delted:", note_found_set.rowcount)
