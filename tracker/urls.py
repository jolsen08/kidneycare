from django.urls import path
from .views import trackerPageView

urlpatterns = [ 
    # path("adduserfood/<int:user_id>/", addUserFoodPageView, name="adduserfood"),
    path("", trackerPageView, name="tracker"), 
]   
