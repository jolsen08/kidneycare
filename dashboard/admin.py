from django.contrib import admin
from .models import Person, FoodConsumption, Food, WaterConsumption

admin.site.register(Person)
# admin.site.register(Condition)
admin.site.register(FoodConsumption)
admin.site.register(Food)
admin.site.register(WaterConsumption)

