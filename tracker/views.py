from django.shortcuts import render

def trackerPageView(request):
    context = {
 
    }
    return render(request, 'tracker/tracker.html', context)

# Create your views here.