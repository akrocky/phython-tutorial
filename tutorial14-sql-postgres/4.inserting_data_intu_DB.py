import psycopg2

connection = psycopg2.connect(
    database="company_sales",
    user="akrocky",
    password="akrocky01",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()
# cursor.execute("SELECT * FROM sale LIMIT 10")
# print(cursor.fetchall())

# cursor.execute("INSERT INTO sale (ORDER_NUM ,ORDER_TYPE,CUST_NAME , PROD_NUMBER ,PROD_NAME ,QUANTITY, PRICE , DISCOUNT,ORDER_TOTAL)  VALUES(1105910,'Retail','Evoluttive Learning','PY999','Complete Python Bootcamp',3,19,0,57) ")
# connection.commit()
cursor.execute("SELECT CUST_NAME, PROD_NAME FROM SALE WHERE ORDER_NUM=1105910")
rows = cursor.fetchall()
print(rows)
connection.close()
