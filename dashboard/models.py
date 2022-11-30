from tkinter import CASCADE
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save 

# class Condition(models.Model) :
#     condition_stage = models.IntegerField()

#     def __str__(self) :
#         self.condition_stage = str(self.condition_stage)
#         return('Kidney Disease Stage ' + self.condition_stage)


class Person(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default="none")
    age = models.IntegerField(default="0")
    height_in = models.IntegerField(default="0")
    weight_lbs = models.IntegerField(default="0")
    highbloodpressure = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    # condition = models.ForeignKey(Condition, on_delete=models.CASCADE, default="1")
    # serum_k_mg_per_dL = models.FloatField(default="0")
    # serum_phos_mg_per_dL_min = models.FloatField(default="0")
    # serum_na_mEq_per_L_min = models.IntegerField(default="0")
    # serum_creatinine_mg_per_dL = models.CharField(max_length=10)
    # serum_creatinine_mg_per_dL = models.CharField(max_length=10)
    # serum_albumin_mg_per_dL = models.FloatField(default="0")
    # serum_blood_sugar_mg_per_dL = models.IntegerField(default="0")


    # def __str__(self) :
    #     full_name = self.first_name + ' ' + self.last_name
    #     return(self.full_name)

    # @property
    # def full_name(self) :
    #     return '%s %s' % (self.first_name, self.last_name)
    
    # def save(self) :
    #     super(Person, self).save()

    def __str__(self) :
        return(self.user.first_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.person.save()

# a.get_profile().DOB

class Food(models.Model) :
    food_name = models.CharField(max_length=100)
    dv_sodium_mg = models.IntegerField()
    dv_protein_g_per_kg_body_weight = models.FloatField()
    dv_k_mg = models.IntegerField()
    dv_phos_mg = models.IntegerField()

    # def __str__(self) :
    #     return(self.food_name)

class FoodConsumption(models.Model) :
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    date_consumed = models.DateField()
    quantity = models.IntegerField()

    # def __str__(self) :
    #     return(self.food_name)

class WaterConsumption(models.Model) :
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    dv_water_L = models.FloatField()
    date_consumed = models.DateField()










