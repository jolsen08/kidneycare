from django.urls import path
from . import views


urlpatterns = [
    path("pdetails/", views.pdetails, name="pdetails"),
    path("pdetails", views.pdetails, name="pdetails"),
    path("sdetails/", views.sdetails, name="sdetails"),
    path("registerdetails", views.registerdetails, name="regdetails"),
    path("serumdetails", views.serumdetails, name="serumdetails"),
    path("register", views.register, name="register"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("home", views.home, name="home"),
    path("accountdetails/", views.account_details, name="accountdetails"),
    path("", views.register, name="register"),

]