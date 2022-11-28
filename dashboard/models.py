from tkinter import CASCADE
from django.db import models
from datetime import datetime

class Condition(models.Model) :
    condition_stage = models.IntegerField()
    sodium_recommendation = models.IntegerField()
    protein_recommendation = models.IntegerField()
    potassium_recommendation = models.IntegerField()
    phosphorus_recommendation = models.IntegerField()

    def __str__(self) :
        return(self.condition_stage)

class Person(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    highbloodpressure = models.BooleanField()
    diabetes = models.BooleanField()
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)

    def full_name(self) :
        return (self.full_name)

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




