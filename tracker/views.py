from django.shortcuts import render
from dashboard.models import Person
from dashboard.models import Food
from dashboard.models import FoodConsumption

def trackerPageView(request):
    data = Person.objects.all()
    food = FoodConsumption.objects.all()
    context = {
        "person": data,
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