from django.contrib import admin
from . import models

admin.site.register(models.Car_model)
admin.site.register(models.Client)
admin.site.register(models.Car)
admin.site.register(models.Order)
admin.site.register(models.Service)
admin.site.register(models.Order_line)
admin.site.register(models.Price)