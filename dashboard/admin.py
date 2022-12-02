from django.contrib import admin
from .models import Person, FoodConsumption, Food, WaterConsumption

# registering our models to be available to the admin
admin.site.register(Person)
admin.site.register(FoodConsumption)
admin.site.register(Food)
admin.site.register(WaterConsumption)

