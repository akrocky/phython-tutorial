import psycopg2


def insert_sale(connection, order_num,

                order_type,    cust_name, prod_number, prod_name, quantity, price, discount):

    order_total = quantity * price
    if discount != 0:
        order_total = order_total * discount
    sale_data = (order_num, order_type, cust_name, prod_number,
                 prod_name, quantity, price, discount, order_total)

    cursor = connection.cursor()
    cursor.execute("""INSERT INTO sale (ORDER_NUM ,ORDER_TYPE,CUST_NAME , PROD_NUMBER ,PROD_NAME ,QUANTITY, PRICE , DISCOUNT,ORDER_TOTAL)  
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", sale_data)

    connection.commit()
    # cursor.execute(
    #     "SELECT CUST_NAME ,ORDER_TOTAL FROM sale WHERE ORDER_NUM=%s", (order_num,))

    # rows = cursor.fetchall()
    # print(f"inserted data is {rows}")


if __name__ == '__main__':

    connection = psycopg2.connect(
        database="company_sales", user="akrocky", password="akrocky01", host="localhost", port="5432")
    order_num = int(input("What is the order number\n"))
    order_type = input("What is the order type\n")
    cust_name = input("What is the cust_name\n")
    prod_number = input("What is the prod_number\n")
    prod_name = input("What is the prod_name\n")
    quantity = float(input("What is the quantity\n"))
    price = float(input("What is the price\n"))
    discount = float(input("What is thediscount\n"))

    insert_sale(connection, order_num,
                order_type,       cust_name,
                prod_number, prod_name, quantity, price, discount)
    connection.close()
