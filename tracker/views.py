from django.shortcuts import render
from dashboard.models import Person
from dashboard.models import Food
from dashboard.models import FoodConsumption
from django.contrib.auth.models import User, auth
from datetime import datetime
from django.shortcuts import redirect

# Returns page, queries database and displays foodconsumption

def trackerPageView(request):
    id = request.user.id
    user = Person.objects.get(user_id = id)
    today = datetime.today()
    foodtoday = FoodConsumption.objects.select_related('person', 'food_name').filter(person_id = id,date_consumed = today).order_by('-date_consumed')
    pastfood = FoodConsumption.objects.filter(person_id = id).exclude(date_consumed = today).order_by('-date_consumed')

    context = {
        "person": user,
        "header" : ["Food Name","Date Consumed","Quantity","Sodium (mg)","Potassium (mg)","Phosphorus (mg)","Protein (g)", "Delete"],
        "foodtoday" : foodtoday,
        "pastfood" : pastfood,
    }
    return render(request, 'tracker/tracker.html', context)

# This pulls data from a form and saves the data to a food. 
# Then it takes that food and adds it to a person, creating a new foodconsumption

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
 
    return redirect(trackerPageView)

# This deletes a food
def deleteUserCustFood(request):
    if request.method == "POST" :
        foodcons_id = request.POST['delete']
        FoodConsumption.objects.filter(id = foodcons_id).delete()

    return redirect('tracker')


# Route to render the add customer food form
def addFoodView(request) :

    return render(request, 'tracker/addcustomfood.html')


