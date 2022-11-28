from django.contrib import admin
from .models import Person, Condition, FoodConsumption

admin.site.register(Person)
admin.site.register(Condition)
admin.site.register(FoodConsumption)

