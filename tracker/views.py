from django.shortcuts import render
from dashboard.models import Person,FoodConsumption

def trackerPageView(request):
    data = Person.objects.all()
    food = FoodConsumption.objects.all()
    context = {
        "person": data,
        "food" : food,
        "header" : ["Food Name","Date Consumed","Quantity"]
    }
    return render(request, 'tracker/tracker.html', context)

# Create your views here.