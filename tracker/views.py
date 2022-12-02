from django.shortcuts import render
from dashboard.models import Person
from dashboard.models import Food
from dashboard.models import FoodConsumption
from django.contrib.auth.models import User, auth
from datetime import datetime
from django.shortcuts import redirect


def trackerPageView(request):
    id = request.user.id
    user = Person.objects.get(user_id = id)
    today = datetime.today()
    foodtoday = FoodConsumption.objects.select_related('person', 'food_name').filter(person_id = id,date_consumed = today).order_by('-date_consumed')
    pastfood = FoodConsumption.objects.filter(person_id = id).exclude(date_consumed = today).order_by('-date_consumed')
    sodiumlist = []
    potassiumlist = []
    phosphoruslist = []
    proteinlist = []
    for i in foodtoday:
         sodiumlist.append(i.food_name.dv_sodium_mg * i.quantity)
    for i in foodtoday:
         potassiumlist.append(i.food_name.dv_k_mg * i.quantity)
    for i in foodtoday:
         phosphoruslist.append(i.food_name.dv_phos_mg * i.quantity)
    for i in foodtoday:
         proteinlist.append(i.food_name.dv_protein_g_per_kg_body_weight * i.quantity)

    

    context = {
        "person": user,
        "header" : ["Food Name","Date Consumed","Quantity","Sodium (mg)","Potassium (mg)","Phosphorus (mg)","Protein (g)", "Delete"],
        "foodtoday" : foodtoday,
        "pastfood" : pastfood,
        "sodiumlist" : sodiumlist,
        "potassiumlist" : potassiumlist,
        "phosphoruslist" : phosphoruslist,
        "proteinlist" : proteinlist
    }
    return render(request, 'tracker/tracker.html', context)


def addUserCustFood(request):
    if request.method == "POST" :
        id = request.user.id
        food = Food()
        food.food_name = request.POST['name']
        food.dv_sodium_mg = request.POST['na']
        food.dv_protein_g_per_kg_body_weight = request.POST['protein']
        food.dv_k_mg = request.POST['potas']
        food.dv_phos_mg = request.POST['phos']
        food.save()
        food_id = food.id

        foodConsump = FoodConsumption()
        foodConsump.person = Person.objects.get(user_id = id)
        foodConsump.food_name = Food.objects.get(id = food_id)
        foodConsump.date_consumed = request.POST['date']
        foodConsump.quantity = request.POST['quantity']
        foodConsump.save()




        # quantity = FoodConsumption.objects.get(quantity = quantity)
 
    return redirect(trackerPageView)

def deleteUserCustFood(request):
    if request.method == "POST" :
        foodcons_id = request.POST['delete']
        FoodConsumption.objects.filter(id = foodcons_id).delete()

    return redirect('tracker')



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