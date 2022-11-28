from django.shortcuts import render

def indexPageView(request):
    context = {
 
    }
    return render(request, 'landingpage/index.html', context)

# Create your views here.
