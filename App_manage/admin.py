from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_per_page = 20



