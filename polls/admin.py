from django.contrib import admin

# Register your models here.

from .models import *


class SoldProductInline(admin.TabularInline):
    model = SoldProduct


@admin.register(TradePointType)
class TradePointTypeDisplay(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(TradePoint)
class TradePointDisplay(admin.ModelAdmin):
    list_display = ("name", "point_type", "point_size", "rent_payment", "utilities_payment", "point_counter_amount")
    inlines = [SoldProductInline]

@admin.register(Employee)
class EmployeeDisplay(admin.ModelAdmin):
    list_display = ("name", "salary", "working_point")


@admin.register(Customer)
class CustomerDisplay(admin.ModelAdmin):
    list_display = ("name", "info")


@admin.register(Product)
class ProductDisplay(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(SomeStore)
class SomeStoreDisplay(admin.ModelAdmin):
    list_display = ("trade_point",)


@admin.register(DepartmentStore)
class DepartmentStoreDisplay(admin.ModelAdmin):
    list_display = ("trade_point",)


# todo fields
@admin.register(Section)
class SectionDisplay(admin.ModelAdmin):
    list_display = ("trade_point", "section_number", "floor", "section_manager")


@admin.register(Hall)
class HallDisplay(admin.ModelAdmin):
    list_display = ("trade_point", "hall_number", "employees_number")


@admin.register(Request)
class RequestDisplay(admin.ModelAdmin):
    list_display = ("trade_point", "date")


class DistributorProductInline(admin.TabularInline):
    model = DistributorProduct


@admin.register(Distributor)
class DistributorDisplay(admin.ModelAdmin):
    list_display = ("name", "contact", "rating")
    inlines = [DistributorProductInline]


@admin.register(ProductsOrder)
class ProductsOrderDisplay(admin.ModelAdmin):
    list_display = ("date", )


class ReceiptItemInline(admin.TabularInline):
    model = ReceiptItem


@admin.register(Receipt)
class ReceiptDisplay(admin.ModelAdmin):
    list_display = ("date", "trade_point", "customer", "employee")
    inlines = [ReceiptItemInline]


@admin.register(ReceiptItem)
class ReceiptItemDisplay(admin.ModelAdmin):
    list_display = ("receipt", "product", "price", "amount")


@admin.register(SoldProduct)
class SoldProductDisplay(admin.ModelAdmin):
    list_display = ("trade_point", "product", "in_stock", "price")


@admin.register(RequestItem)
class RequestItemDisplay(admin.ModelAdmin):
    list_display = ("request", "product", "amount")


@admin.register(DistributorProduct)
class DistributorProductDisplay(admin.ModelAdmin):
    list_display = ("distributor", "product", "price", "offer_start_date", "offer_end_date")


@admin.register(ProductOrderItem)
class ProductsOrderItemDisplay(admin.ModelAdmin):
    list_display = ("products_order", "distributor_product", "amount", "price")


@admin.register(RequestOrder)
class RequestOrderDisplay(admin.ModelAdmin):
    list_display = ("request", "order")
