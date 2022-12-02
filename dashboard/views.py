# importing the appropriate packages and models
import json
from django.shortcuts import render
import json
import psycopg2
from django.db.models import Sum
from dashboard.models import FoodConsumption, Food, Person
from datetime import datetime, timedelta, time, date

def dashboardPageView(request):
    # totals (combines all of the micronutrients and protein into one value to display). We don't have this in our program
    # but may be handy at some point in the future.
    try:
        # connecting to the database and querying for the values we are searching for. We repeat this pattern for each micronutrient
        # as well as protein
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

        # converting the results into a dictionary (keys and values) and a list (values). This will be used each time the
        # dashboard page is refreshed or opened
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


    # sodium
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


    # k (potassium)
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


    # protein
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

    # creating variables to be used in the daily journal display
    totalsod,totalk,totalpro,totalphos,pctphos,pctsod,pctk,pctpro,proteinmax = dailyBars(request)
    protcolor = "bg-success"
    phoscolor = "bg-success"
    sodcolor = "bg-success"
    potasscolor = "bg-success"

    # assigning the proper colors according to micronutrient levels
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

    # declaring attributes to be used and assigning them values based on the CKD stage of the user
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

    # the default values will be for users who are in stage 3 or 4 of CKD, since we are catering mostly to them. 
    else :
        sodamount = 2300
        kamount = 3000
        phosamount = 1000
        proteinamount = .6
        sodmin = 1495
        kmin = 2500
        phosmin = 800

    # setting mins equal to maxes if there is no min (this is important for the micronutrient visualizations)
    if sodmin == 0:
        sodmin = sodamount

    if phosmin == 0:
        phosmin = phosamount

    if kmin == 0:
        kmin = kamount

    # calculating the percent of totals for the user  
    pctsod = round((totalsod/sodamount)*100,2)
    pctk = (totalk/kamount)*100
    pctphos = (totalphos/phosamount)*100

    # declaring variables to be referenced in the dashboard.html page      
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

# this function updates the daily journal values
def dailyBars(request):
    stage = request.user.person.condition
    id = request.user.id
    totalsod = 0
    totalk = 0
    totalpro = 0
    totalphos = 0
    today = datetime.today()
    personresult = Person.objects.filter(id = id)
    weight = personresult[0].weight_lbs
    # only accepting foods eaten today
    foodComp = FoodConsumption.objects.select_related('person', 'food_name').filter(person_id = id,date_consumed = today)

    # for loop to add values for each micronutrient and protein
    for i in foodComp:
        totalsod = totalsod + (i.food_name.dv_sodium_mg * i.quantity)
    for i in foodComp:
        totalk = totalk + (i.food_name.dv_k_mg * i.quantity)
    for i in foodComp:
        totalphos= totalphos+ (i.food_name.dv_phos_mg * i.quantity)
    for i in foodComp:
        totalpro = totalpro + (i.food_name.dv_protein_g_per_kg_body_weight * i.quantity)
    
    # again adjusting the recommended values for each micronutrient based on user CKD stage
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

    # calculating the percent totals to appear in the dashboard   
    pctsod = round((totalsod/sodamount)*100,2)
    pctk = (totalk/kamount)*100
    pctphos = (totalphos/phosamount)*100
    proteinconsump = weight * proteinamount
    pctpro = (totalpro/proteinconsump) * 100
    proteinmax = proteinconsump

    # declaring variables in the context to be used in the html page
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
    # returning all the variables
    return totalsod,totalk,totalpro,totalphos,pctphos,pctsod,pctk,pctpro,proteinmax