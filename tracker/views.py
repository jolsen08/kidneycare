from django.shortcuts import render

def trackerPageView(request):
    data = Person.object.all()
    context = {
        "person": data
    }
    return render(request, 'tracker/tracker.html', context)

# Create your views here.