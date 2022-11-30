from django.shortcuts import render
from dashboard.models import Person,FoodConsumption

def trackerPageView(request):
    data = Person.objects.all()
    food = FoodConsumption.objects.all()
    context = {
        "person": data,
        "food" : food
    }
    return render(request, 'tracker/tracker.html', context)

# Create your views here.