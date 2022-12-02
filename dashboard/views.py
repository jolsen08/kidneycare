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
        
        print(dicttotal)

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
        id = request.user.id
        connection = psycopg2.connect(user="postgres",
            password="admin123",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, sodiumsum from (select date_consumed, person_id, sum(dv_sodium_mg * quantity) as sodiumsum from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed, person_id order by date_consumed)sq1 where sq1.person_id = %(id)s;"

        cursor.execute(postgreSQL_select_Query,{'id':id})
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
        id = request.user.id
        connection = psycopg2.connect(user="postgres",
            password="admin123",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, ksum from (select date_consumed, person_id, sum(dv_k_mg * quantity) as ksum from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed, person_id order by date_consumed)sq1 where sq1.person_id = %(id)s;"

        cursor.execute(postgreSQL_select_Query,{'id':id})
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
        id = request.user.id
        connection = psycopg2.connect(user="postgres",
            password="admin123",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, phossum from (select date_consumed, person_id, sum(dv_phos_mg * quantity) as phossum from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed, person_id order by date_consumed)sq1 where sq1.person_id = %(id)s;"

        cursor.execute(postgreSQL_select_Query,{'id':id})
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
        id = request.user.id
        connection = psycopg2.connect(user="postgres",
            password="admin123",
            host="localhost",
            port="5432",
            database="intex2")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select date_consumed, proteinsum from (select date_consumed, person_id, sum(dv_protein_g_per_kg_body_weight * quantity) as proteinsum from dashboard_foodconsumption dfc inner join dashboard_food df on dfc.food_name_id = df.id group by date_consumed, person_id order by date_consumed)sq1 where sq1.person_id = %(id)s;"

        cursor.execute(postgreSQL_select_Query,{'id':id})
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

    # personresult = Person.objects.filter(id = id)
    # weight = request.user.person.weight_lbs
    stage = request.user.person.condition
    sodmin = 0
    phosmin = 0
    kmin = 0
    
    if stage == 'normal' :
        sodamount = 2300
        kamount = 3500
        phosamount = 3000
        proteinamount = .8
       
    elif stage == 'dialysis' :
        sodamount = 2000
        kamount = 2000
        phosamount = 1000
        proteinamount = 1.2,
        sodmin = 750
        phosmin = 800
      
    else :
        sodamount = 2300
        kamount = 3000
        phosamount = 1000
        proteinamount = .6
        sodmin = 1495
        kmin = 2500
        phosmin = 800

    if sodmin == 0:
        sodmin = sodamount

    if phosmin == 0:
        phosmin = phosamount

    if kmin == 0:
        kmin = kamount
        
    pctsod = round((totalsod/sodamount)*100,2)
    pctk = (totalk/kamount)*100
    pctphos = (totalphos/phosamount)*100
    # proteinconsump = weight * proteinamount
    # pctpro = (totalpro/proteinconsump) * 100
    # proteinmax = proteinconsump
        
           
    context = {
        'datasodium': dictsodium,
        'valuessodium': listsodium,
        'datak' : dictk,
        'valuesk' : listk,
        'dataphos' : dictphos,
        'valuesphos' : listphos,
        'dataprotein' : dictprotein,
        'valuesprotein' : listprotein,
        'sodamount' : sodamount,
        'kamount' : kamount,
        'phosamount' : phosamount,
        'proteinamount' : proteinamount,
        "sodmin" : sodmin,
        "phosmin" : phosmin,
        "kmin" : kmin,
        
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
    stage = request.user.person.condition
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
    
    if stage == 'normal' :
        sodamount = 2300
        kamount = 3500
        phosamount = 3000
        proteinamount = .8
       
    elif stage == 'dialysis' :
        sodamount = 2000
        kamount = 2000
        phosamount = 1000
        proteinamount = 1.2
      
    else :
        sodamount = 2300
        kamount = 3000
        phosamount = 1000
        proteinamount = .6
        
    pctsod = round((totalsod/sodamount)*100,2)
    pctk = (totalk/kamount)*100
    pctphos = (totalphos/phosamount)*100
    proteinconsump = weight * proteinamount
    pctpro = (totalpro/proteinconsump) * 100
    proteinmax = proteinconsump

    print(str(kamount))

    context = {
        "totalsod" : round(totalsod,2),
        "totalk" : round(totalk,2),
        "totalpro" : totalpro,
        "totalphos" : totalphos,
        "pctsod" : round(pctsod,2),
        "pctk" : round(pctk,2),
        "pctpro" : pctpro,
        "pctphos" : round(pctphos,2),
        "proteinmax" : proteinconsump,
        "sodamount" : round(sodamount,2),
        "kamount" : round(kamount,2),
        "phosamount" : round(phosamount,2),
    }
    print(totalpro)
    print(proteinconsump)
    return totalsod,totalk,totalpro,totalphos,pctphos,pctsod,pctk,pctpro,proteinmax
    # required values & current daily amounts