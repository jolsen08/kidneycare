import json
from django.shortcuts import render
# from .query import dictsodium, listsodium, dictk, listk, dictphos, listphos, dictprotein, listprotein
import json
import psycopg2
from django.db.models import Sum
from dashboard.models import FoodConsumption, Food, Person
from datetime import datetime, timedelta, time, date




def dashboardPageView(request):
    # totals
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
            password="admin123",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, sum(dv_sodium_mg * quantity) from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed, dfc.person_id order by date_consumed"

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
            password="admin123",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, sum(dv_k_mg * quantity) from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed order by date_consumed"

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
            password="admin123",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, sum(dv_phos_mg * quantity) from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed order by date_consumed"

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
            password="admin123",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, sum(dv_protein_g_per_kg_body_weight * quantity) from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed order by date_consumed"

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
    totalsod,totalk,totalpro,totalphos,pctphos,pctsod,pctk,pctpro,proteinmax = dailyBars(request)
    protcolor = "bg-success"
    phoscolor = "bg-success"
    sodcolor = "bg-success"
    potasscolor = "bg-success"

    if pctphos > 100:
        phoscolor = "bg-danger"
    elif pctphos > 75:
        phoscolor = "bg-warning"

    if pctsod > 100:
        sodcolor = "bg-danger"
    elif pctsod > 75:
        sodcolor = "bg-warning"

    if pctk > 100:
        potasscolor = "bg-danger"
    elif pctk > 75:
        potasscolor = "bg-warning"

    if pctpro > 100:
        protcolor = "bg-danger"
    elif pctpro > 75:
        protcolor = "bg-warning"
        
           
    context = {
        'datasodium': dictsodium,
        'valuessodium': listsodium,
        'datak' : dictk,
        'valuesk' : listk,
        'dataphos' : dictphos,
        'valuesphos' : listphos,
        'dataprotein' : dictprotein,
        'valuesprotein' : listprotein,

        'totalsod' : totalsod,
        'totalk' : totalk,
        'totalpro' : totalpro,
        'totalphos' : totalphos,

        'pctphos' : pctphos, 
        'pctsod' : pctsod,
        'pctk' : pctk,  
        'pctpro' : pctpro,  
        'proteinmax' : proteinmax, 

        'protcolor' : protcolor,
        'phoscolor' : phoscolor,
        'sodcolor' : sodcolor,
        'potasscolor' : potasscolor,

          }
    return render(request, 'dashboard/dashboard.html', context)

def dailyBars(request):
    # get current total value of sodium
    id = request.user.id
    totalsod = 0
    totalk = 0
    totalpro = 0
    totalphos = 0
    today = datetime.today()
    personresult = Person.objects.filter(id = id)
    weight = personresult[0].weight_lbs
    foodComp = FoodConsumption.objects.select_related('person', 'food_name').filter(person_id = id,date_consumed = today)
    # for i in foodComp:
    for i in foodComp:
        totalsod = totalsod + (i.food_name.dv_sodium_mg * i.quantity)
    for i in foodComp:
        totalk = totalk + (i.food_name.dv_k_mg * i.quantity)
    for i in foodComp:
        totalphos= totalphos+ (i.food_name.dv_phos_mg * i.quantity)
    for i in foodComp:
        totalpro = totalpro + (i.food_name.dv_protein_g_per_kg_body_weight * i.quantity)

    proteinconsump = weight * 0.6
    pctpro = (totalpro/proteinconsump) * 100
    pctsod = round((totalsod/2000)*100,2)
    pctk = (totalk/2750)*100
    pctphos = (totalphos/900)*100
    proteinmax = proteinconsump

    context = {
        "totalsod" : round(totalsod,2),
        "totalk" : round(totalk,2),
        "totalpro" : totalpro,
        "totalphos" : round(totalphos,2),
        "pctsod" : round((totalsod/2000)*100,2),
        "pctk" : (totalk/2750)*100,
        "pctpro" : pctpro,
        "pctphos" : (totalphos/900)*100,
        "proteinmax" : round(proteinconsump,2)

    }

    return totalsod,totalk,totalpro,totalphos,pctphos,pctsod,pctk,pctpro,proteinmax
    # required values & current daily amounts