from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Dish, DishType, Cook

admin.site.register(Dish)
admin.site.register(DishType)
admin.site.register(Cook, UserAdmin)
