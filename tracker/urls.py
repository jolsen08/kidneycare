from django.urls import path
from .views import addConsumed, addFoodView, trackerPageView, addUserFoodPageView

urlpatterns = [ 
    path("adduserfood/", addUserFoodPageView, name="adduserfood"),
    path("", trackerPageView, name="tracker"), 
    path("addfooddata/", addFoodView, name="fooddata"),
]   
