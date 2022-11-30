import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
        password="password",
        host="localhost",
        port="5432",
        database="intex2")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select date_consumed, count(quantity) from dashboard_foodconsumption group by date_consumed"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from foodconsumption table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("Date_Consumed = ", row[0], )
        print("Quantity = ", row[1])

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")