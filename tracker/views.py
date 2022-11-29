from django.shortcuts import render
from dashboard.models import Person

def trackerPageView(request):
    data = Person.objects.all()
    context = {
        "person": data
    }
    return render(request, 'tracker/tracker.html', context)

# Create your views here.