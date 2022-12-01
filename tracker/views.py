from django.shortcuts import render
from dashboard.models import Person
from dashboard.models import Food
from dashboard.models import FoodConsumption
from django.contrib.auth.models import User, auth
from datetime import datetime, timedelta, time, date

def trackerPageView(request):
    # data = Person.objects.all()
    # user = Person.objects.get(user_id=id)
    id = request.user.id
    user = Person.objects.get(user_id = id)
    food = FoodConsumption.objects.filter(person_id = id,)
    

    context = {
        "person": user,
        "food" : food,
        "header" : ["Food Name","Date Consumed","Quantity"]
    }
    return render(request, 'tracker/tracker.html', context)


def addUserFoodPageView(request):
    if request.method == "POST" :
        # id = request.POST['user_id']
        # quantity = FoodConsumption.objects.get(quantity = quantity)
        food = Food()
        food.food_name = request.POST['food_name']
        food.dv_sodium_mg = request.POST['dv_sodium_mg']
        food.dv_protein_g_per_kg_body_weight = request.POST['dv_protein_g_per_kg_body_weight']
        food.dv_k_mg = request.POST['dv_k_mg']
        food.dv_phos_mg = request.POST['dv_phos_mg']

        food.save()
    return render(request, 'tracker/food.html')

def addFoodConsumed(request) :
    if request.method == "POST" :
        person_id = request.POST['user_id']
        consumed = FoodConsumption.objects.get(user_id=person_id)

        food = request.POST['food_name']
        consumed.food_name.add(Food.objects.get(id=food))
        consumed.date_consumed = request.POST['date_consumed']
        consumed.quantity = request.POST['quantity']
    
    return render(request, 'tracker/consume.html')



def addFoodData(request, user_id) :
    holder = FoodConsumption.objects.get(id = user_id)
    data = Food()
    foods = data.food_name
    sodium = data.dv_sodium_mg
    protein = data.dv_protein_g_per_kg_body_weight
    k = data.dv_k_mg
    phos = data.dv_phos_mg


    avail_food = FoodConsumption.objects.exclude(id__in=FoodConsumption.food_name)

    context = {
        "record" : data,
        "food" : foods,
        "sodium" : sodium,
        "protein" : protein,
        "k" : k,
        "phos" : phos,
        "avail" : avail_food
    }

    return render(request, 'tracker/food.html', context)

def addConsumed(request, user_id) :
    holder = FoodConsumption.objects.get(id = user_id)
    data = FoodConsumption()
    data2 = Food()
    foods = data.food_name_id
    date_consumed = data.date_consumed
    quantity = data.quantity


    avail_consume = Food.objects.exclude(id__in=Food.food_name)

    context = {
        "record" : data,
        "food" : foods,
        "date_consumed" : date_consumed, 
        "quantity" : quantity,
        "avail" : avail_consume,
    }

    return render(request, 'tracker/consume.html', context)