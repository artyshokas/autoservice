from django.contrib import admin
from . import models


class OrderlineInline(admin.TabularInline):
    model = models.Order_line
    extra = 0
    can_delete = True

class OrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'date', 'total')
    inlines = (OrderlineInline, )


class OrderlineAdmin(admin.ModelAdmin):
    pass



class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'owner', 'number', 'vin', )
    list_filter = ('owner', 'car_name', )
    search_fields = ('number', 'vin', )


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(models.Car_model)
admin.site.register(models.Client)
admin.site.register(models.Car, CarAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Order_line, OrderlineAdmin)
admin.site.register(models.Price)