from django.urls import path
from . import views


urlpatterns = [
    path("pdetails/", views.pdetails, name="pdetails"),
    path("pdetails", views.pdetails, name="pdetails"),
    path("registerdetails", views.registerdetails, name="regdetails"),
    path("register", views.register, name="register"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("home", views.home, name="home"),
    path("", views.register, name="register"),

]