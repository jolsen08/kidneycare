from django.shortcuts import render
from dashboard.models import Person
from dashboard.models import Food
from dashboard.models import FoodConsumption
from django.contrib.auth.models import User, auth
from datetime import datetime, timedelta, time, date

def trackerPageView(request):
    id = request.user.id
    user = Person.objects.get(user_id = id)
    today = datetime.today()
    food = FoodConsumption.objects.filter(person_id = id, date_consumed = today)
    pastfood = FoodConsumption.objects.filter(person_id = id).exclude(date_consumed = today).order_by('-date_consumed')

    

    context = {
        "person": user,
        "food" : food,
        "header" : ["Food Name","Date Consumed","Quantity"],
        "pastfood" : pastfood
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

# def addFoodConsumed(request) :
#     if request.method == "POST" :
#         person_id = request.POST['user_id']
#         consumed = FoodConsumption.objects.get(user_id=person_id)

#         food = request.POST['food_name']
#         consumed.food_name.add(Food.objects.get(id=food))
#         consumed.date_consumed = request.POST['date_consumed']
#         consumed.quantity = request.POST['quantity']
    
#     return render(request, 'tracker/consume.html')



def addFoodView(request) :

    return render(request, 'tracker/addcustomfood.html')

def addConsumed(request, user_id) :
    data = FoodConsumption.objects.get(id = user_id)
    foods = data.food_name  
    date_consumed = data.date_consumed
    quantity = data.quantity
    foodavail = Food.food_name


    #avail_consume = Food.objects.get(id__in=data.food_name)

    context = {
        "record" : data,
        "food" : foods,
        "date_consumed" : date_consumed, 
        "quantity" : quantity,
        "avail" : foodavail,
    }

    return render(request, 'tracker/consume.html', context)