# importing the appropriate packages and models
from tkinter import CASCADE
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save 

# Creating the person model, including condition and serum levels and connecting to the user class with a one to one relationship
class Person(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default="none")
    age = models.IntegerField(default="0")
    height_in = models.IntegerField(default="0")
    weight_lbs = models.IntegerField(default="0")
    highbloodpressure = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    condition = models.CharField(max_length=20, default="0")
    serum_k_mg_per_dL = models.FloatField(default="0")
    serum_phos_mg_per_dL_min = models.FloatField(default="0")
    serum_na_mEq_per_L_min = models.FloatField(default="0")
    serum_creatinine_mg_per_dL = models.FloatField(default="0")
    serum_albumin_mg_per_dL = models.FloatField(default="0")
    serum_blood_sugar_mg_per_dL = models.FloatField(default="0")

    # returning the full name to the admin
    def __str__(self) :
        self.user.first_name = self.user.first_name.upper()
        return(self.user.first_name)

    # returning the user
    def __str__(self) :
        return(str(self.user))

# saves and updates person whenever user is saved or updated
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.person.save()

# the remaining models in our database
class Food(models.Model) :
    food_name = models.CharField(max_length=100)
    dv_sodium_mg = models.FloatField()
    dv_protein_g_per_kg_body_weight = models.FloatField()
    dv_k_mg = models.FloatField()
    dv_phos_mg = models.FloatField()

    def __str__(self) :
        self.food_name = self.food_name.upper()
        return(self.food_name)

class FoodConsumption(models.Model) :
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    date_consumed = models.DateField()
    quantity = models.IntegerField()

    def __str__(self) :
        self.food_name.food_name = self.food_name.food_name.upper()
        return(self.food_name.food_name)

class WaterConsumption(models.Model) :
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    dv_water_L = models.FloatField()
    date_consumed = models.DateField()










