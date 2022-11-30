from django.urls import path
from .views import trackerPageView
from .views import addUserFoodPageView

urlpatterns = [ 
    # path("adduserfood/<int:user_id>/", addUserFoodPageView, name="adduserfood"),
    path("", trackerPageView, name="tracker"), 
]   
