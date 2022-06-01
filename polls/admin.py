from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(TradePointType)
admin.site.register(TradePoint)
admin.site.register(SomeStore)
admin.site.register(DepartmentStore)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Receipt)


@admin.register(ReceiptItem)
class ReceiptItemAdmin(admin.ModelAdmin):
    list_display = ("receipt", "product", "amount")


admin.site.register(Section)
admin.site.register(Hall)
admin.site.register(SoldProduct)
admin.site.register(Distributor)
admin.site.register(Request)
admin.site.register(RequestItem)
admin.site.register(DistributorProduct)
admin.site.register(ProductsOrder)
admin.site.register(ProductOrderItem)
admin.site.register(RequestOrder)
