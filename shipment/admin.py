from django.contrib import admin
from.models import Shipping
# Register your models here.
class ShippingAdmin(admin.ModelAdmin):
    display_list=('name','address','phone_number','distance')
admin.site.register(Shipping,ShippingAdmin)