from django.contrib import admin

# Register your models here.

from .models import Plant, Tip, Category, Subcategory, Sun_Exposure, Soil_Type, Soil_Moisture, Habit

# Register your models here.
admin.site.register(Plant)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Tip)
admin.site.register(Sun_Exposure)
admin.site.register(Soil_Type)
admin.site.register(Soil_Moisture)
admin.site.register(Habit)
