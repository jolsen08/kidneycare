from django.shortcuts import render

def indexPageView(request):
    context = {
 
    }
    return render(request, 'base.html', context)

# Create your views here.
