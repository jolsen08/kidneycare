import json
from django.shortcuts import render
# from .query import dictsodium, listsodium, dictk, listk, dictphos, listphos, dictprotein, listprotein
import json
import psycopg2

def dashboardPageView(request):
    try:
        connection = psycopg2.connect(user="postgres",
            password="password",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, (sodium + k + protein + phos) as total from (select date_consumed, sum(dv_sodium_mg * quantity) as sodium, sum(dv_protein_g_per_kg_body_weight * quantity) as protein, sum(dv_k_mg * quantity) as k, sum(dv_phos_mg * quantity) as phos from dashboard_foodconsumption inner join dashboard_food on dashboard_foodconsumption.food_name_id = dashboard_food.id group by date_consumed order by date_consumed)sq1 order by date_consumed"

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from foodconsumption table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        listtotal = []
        dicttotal = {}
    
        for row in mobile_records:
            dicttotal[row[0]] = row[1]
            listtotal.append(dicttotal[row[0]])

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
        postgreSQL_select_Query = "select date_consumed, sum(dv_sodium_mg) from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed, dfc.person_id order by date_consumed"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        listsodium = []
        dictsodium = {}

        for row in mobile_records:
            dictsodium[row[0]] = row[1]
            listsodium.append(dictsodium[row[0]])

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
        mobile_records = cursor.fetchall()

        listk = []
        dictk = {}
   
        for row in mobile_records:
            dictk[row[0]] = row[1]
            listk.append(dictk[row[0]])

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
            # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    #phos
    try:
        connection = psycopg2.connect(user="postgres",
            password="password",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, sum(dv_phos_mg) from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed order by date_consumed"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        listphos = []
        dictphos = {}
       
        for row in mobile_records:     
            dictphos[row[0]] = row[1]
            listphos.append(dictphos[row[0]])

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
            # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    #protein
    try:
        connection = psycopg2.connect(user="postgres",
            password="password",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, sum(dv_protein_g_per_kg_body_weight) from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed order by date_consumed"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        listprotein = []
        dictprotein = {}
        for row in mobile_records:
            dictprotein[row[0]] = row[1]
            listprotein.append(dictprotein[row[0]])

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
            # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    context = {
        'datasodium': dictsodium,
        'valuessodium': listsodium,
        'datak' : dictk,
        'valuesk' : listk,
        'dataphos' : dictphos,
        'valuesphos' : listphos,
        'dataprotein' : dictprotein,
        'valuesprotein' : listprotein,
    }
    return render(request, 'dashboard/dashboard.html', context)

