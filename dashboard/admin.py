from django.contrib import admin
from .models import Person, FoodConsumption, Condition

admin.site.register(Person)
admin.site.register(FoodConsumption)
admin.site.register(Condition)

