import psycopg2
# import pandas as pd
# import seaborn as sns
import json

#totals
try:
    connection = psycopg2.connect(user="postgres",
        password="admin123",
        host="localhost",
        port="5432",
        database="intex2")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select date_consumed, (sodium + k + protein + phos) as total from (select date_consumed, sum(dv_sodium_mg * quantity) as sodium, sum(dv_protein_g_per_kg_body_weight * quantity) as protein, sum(dv_k_mg * quantity) as k, sum(dv_phos_mg * quantity) as phos from dashboard_foodconsumption inner join dashboard_food on dashboard_foodconsumption.food_name_id = dashboard_food.id group by date_consumed order by date_consumed)sq1 order by date_consumed"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from foodconsumption table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print(mobile_records)
    listtotal = []
    dicttotal = {}
    print("Print each row and it's columns values")
    for row in mobile_records:
        print("Date_Consumed = ", row[0], )
        print("total micro-macro nutrients = ", row[1])
        dicttotal[row[0]] = row[1]
        listtotal.append(dicttotal[row[0]])
        # print("dv_protein_g_per_kg_body_weight = ", row[2])
        # print("dv_k_mg = ", row[3])
        # print("dv_phos_mg", row[4])
    
    with open('data.json', 'w') as f:
        json.dump(str(dicttotal), f)

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
        # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


#sodium
try:
    connection = psycopg2.connect(user="postgres",
        password="password",
        host="localhost",
        port="5432",
        database="intex2")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select date_consumed, sum(dv_sodium_mg) from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed order by date_consumed"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from foodconsumption table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print(mobile_records)
    listsodium = []
    dictsodium = {}
    print("Print each row and it's columns values")
    for row in mobile_records:
        print("Date_Consumed = ", row[0], )
        print("total sodium = ", row[1])
        dictsodium[row[0]] = row[1]
        listsodium.append(dictsodium[row[0]])
        # print("dv_protein_g_per_kg_body_weight = ", row[2])
        # print("dv_k_mg = ", row[3])
        # print("dv_phos_mg", row[4])
    
    with open('data.json', 'w') as f:
        json.dump(str(dictsodium), f)

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
        # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


#k
try:
    connection = psycopg2.connect(user="postgres",
        password="password",
        host="localhost",
        port="5432",
        database="intex2")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select date_consumed, sum(dv_k_mg) from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed order by date_consumed"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from foodconsumption table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print(mobile_records)
    listk = []
    dictk = {}
    print("Print each row and it's columns values")
    for row in mobile_records:
        print("Date_Consumed = ", row[0], )
        print("total potassium = ", row[1])
        dictk[row[0]] = row[1]
        listk.append(dictk[row[0]])
        # print("dv_protein_g_per_kg_body_weight = ", row[2])
        # print("dv_k_mg = ", row[3])
        # print("dv_phos_mg", row[4])
    
    with open('data.json', 'w') as f:
        json.dump(str(dictk), f)

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
        # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
