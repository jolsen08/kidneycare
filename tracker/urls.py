from django.urls import path
from .views import trackerPageView

urlpatterns = [ 
    path("", trackerPageView, name="index"), 
]   
