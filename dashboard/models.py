from tkinter import CASCADE
from django.db import models
from datetime import datetime

class Condition(models.Model) :
    condition_stage = models.IntegerField()
    serum_k_mg_per_dL_min = models.FloatField()
    serum_k_mg_per_dL_max = models.FloatField()
    serum_phos_mg_per_dL_min = models.FloatField()
    serum_phos_mg_per_dL_max = models.FloatField()
    serum_na_mEq_per_L_min = models.IntegerField()
    serum_na_mEq_per_L_max = models.IntegerField()
    serum_creatinine_mg_per_dL_men = models.CharField(max_length=10)
    serum_creatinine_mg_per_dL_women = models.CharField(max_length=10)
    serum_albumin_mg_per_dL = models.FloatField()
    serum_blood_sugar_mg_per_dL_min = models.IntegerField()
    serum_blood_sugar_mg_per_dL_max = models.IntegerField()
    dv_sodium_recommendation_mg_min = models.IntegerField()
    dv_sodium_recommendation_mg_max = models.IntegerField()
    dv_protein_recommendation_g_per_kg_body_weight = models.FloatField()
    dv_water_recommendation_L_min_men = models.FloatField()
    dv_water_recommendation_L_max_men = models.FloatField()
    dv_water_recommendation_L_min_women = models.FloatField()
    dv_water_recommendation_L_max_women = models.FloatField()
    dv_k_recommendation_mg_min = models.IntegerField()
    dv_k_recommendation_mg_max = models.IntegerField()
    dv_phos_recommendation_mg_min = models.IntegerField()
    dv_phos_recommendation_mg_max = models.IntegerField()

    def __str__(self) :
        self.condition_stage = str(self.condition_stage)
        return('Kidney Disease Stage ' + self.condition_stage)

class Gender(models.Model) :
    gender = models.CharField(max_length=10)

    def __str__(self) :
        return(self.gender)

class Person(models.Model) :
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
    dv_sodium_mg = models.IntegerField()
    dv_protein_g_per_kg_body_weight = models.FloatField()
    dv_water_L = models.FloatField()
    dv_k_mg = models.IntegerField()
    dv_phos_mg = models.IntegerField()

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


class FoodConsumption(models.Model) :
    food_name = models.CharField(max_length=100)
    date_consumed = models.DateField()
    quantity = models.IntegerField()

    def __str__(self) :
        return(self.food_name)






