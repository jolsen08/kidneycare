from django.urls import path
from .views import addConsumed, addFoodData, trackerPageView, addUserFoodPageView, addFoodConsumed

urlpatterns = [ 
    path("adduserfood/", addUserFoodPageView, name="adduserfood"),
    path("addconsumption/", addFoodConsumed, name="addconsumption"),
    path("", trackerPageView, name="tracker"), 
    path("addfooddata/<int:user_id>/", addFoodData, name="fooddata"),
    path("addconsumed/<int:user_id>/", addConsumed, name="addconsumed"),
]   
