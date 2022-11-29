from tkinter import CASCADE
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save 

class Condition(models.Model) :
    condition_stage = models.IntegerField()

    def __str__(self) :
        self.condition_stage = str(self.condition_stage)
        return('Kidney Disease Stage ' + self.condition_stage)

class Gender(models.Model) :
    gender = models.CharField(max_length=10)

    def __str__(self) :
        return(self.gender)

class Person(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    age = models.IntegerField()
    height_in = models.IntegerField()
    weight_lbs = models.IntegerField()
    highbloodpressure = models.BooleanField()
    diabetes = models.BooleanField()
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    serum_k_mg_per_dL = models.FloatField()
    serum_phos_mg_per_dL_min = models.FloatField()
    serum_na_mEq_per_L_min = models.IntegerField()
    serum_creatinine_mg_per_dL = models.CharField(max_length=10)
    serum_creatinine_mg_per_dL = models.CharField(max_length=10)
    serum_albumin_mg_per_dL = models.FloatField()
    serum_blood_sugar_mg_per_dL = models.IntegerField()

    def __str__(self) :
        full_name = self.first_name + ' ' + self.last_name
        return(self.full_name)

    @property
    def full_name(self) :
        return '%s %s' % (self.first_name, self.last_name)
    
    def save(self) :
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(Person, self).save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # instance.profile.save()
    instance.person.save()

# a.get_profile().DOB

class Food(models.Model) :
    food_name = models.CharField(max_length=100)
    dv_sodium_mg = models.IntegerField()
    dv_protein_g_per_kg_body_weight = models.FloatField()
    dv_k_mg = models.IntegerField()
    dv_phos_mg = models.IntegerField()

    def __str__(self) :
        return(self.food_name)

class FoodConsumption(models.Model) :
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    date_consumed = models.DateField()
    quantity = models.IntegerField()

class WaterConsumption(models.Model) :
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    dv_water_L = models.FloatField()
    date_consumed = models.DateField()










