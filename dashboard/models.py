from tkinter import CASCADE
from django.db import models
from datetime import datetime

class Condition(models.Model) :
    condition_stage = models.IntegerField()
    sodium_recommendation_mg_min = models.IntegerField()
    sodium_recommendation_mg_max = models.IntegerField()
    protein_recommendation_g_per_kg_body_weight = models.FloatField()
    water_recommendation_L_min_men = models.FloatField()
    water_recommendation_L_max_men = models.FloatField()
    water_recommendation_L_min_women = models.FloatField()
    water_recommendation_L_max_women = models.FloatField()
    potassium_recommendation_mg_min = models.IntegerField()
    potassium_recommendation_mg_max = models.IntegerField()
    phosphorus_recommendation_mg_min = models.IntegerField()
    phosphorus_recommendation_mg_max = models.IntegerField()

    def __str__(self) :
        self.condition_stage = str(self.condition_stage)
        return('Kidney Disease Stage ' + self.condition_stage)

class Person(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    height_in = models.IntegerField()
    weight_lbs = models.IntegerField()
    highbloodpressure = models.BooleanField()
    diabetes = models.BooleanField()
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)

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




