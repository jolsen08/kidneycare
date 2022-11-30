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
    food = FoodConsumption.objects.filter(person_id = id)

    context = {
        "person": user,
        "food" : food,
        "header" : ["Food Name","Date Consumed","Quantity"]
    }
    return render(request, 'tracker/tracker.html', context)


# def addUserFoodPageView(request):
#     if request.method == "POST" :
#         id = request.POST['user_id']
#         quantity = FoodConsumption.objects.get(quantity = quantity)
#         food = Food.objects.get(user_id = id)
#         food.food_name = request.POST['food_name']
#         food.dv_sodium_mg = request.POST['dv_sodium_mg']
#         food.dv_protein_g_per_kg_body_weight = request.POST['dv_protein_g_per_kg_body_weight']
#         food.dv_k_mg = request.POST['dv_k_mg']
#         food.dv_phos_mg = request.POST['dv_phos_mg']

#         food.save()

#         return render(request, 'tracker/tracker.html')

#     else :
#         return render(request, 'tracker/tracker.html')

# Create your views here.