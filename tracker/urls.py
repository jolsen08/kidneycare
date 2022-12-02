from django.urls import path
from .views import addConsumed, addFoodView, trackerPageView, addUserCustFood, deleteUserCustFood

urlpatterns = [ 
    path("adduserfood", addUserCustFood, name="adduserfood"),
    path("deleteuserfood", deleteUserCustFood, name="adduserfood"),
    path("", trackerPageView, name="tracker"), 
    path("addfooddata/", addFoodView, name="fooddata"),
]   
