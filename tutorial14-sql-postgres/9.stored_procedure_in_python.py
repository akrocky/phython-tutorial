import psycopg2

if __name__ == "__main__":
    connection = psycopg2.connect(database="company_sales",
                                  user="akrocky",
                                  password="akrocky01",
                                  host="localhost",
                                  port="5432"
                                  )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute('''CALL return_nondiscounted_item(%s,%s)''', (1105910, 1))
    connection.close()
