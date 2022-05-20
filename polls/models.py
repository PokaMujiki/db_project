from django.db import models
from django.db.models import UniqueConstraint

from polls.validators import *


# Create your models here.


class TradePointType(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])


class TradePoint(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])
    point_type = models.ForeignKey(TradePointType, on_delete=models.PROTECT)
    point_size = models.IntegerField(null=True, blank=True, validators=[validate_gt_0])
    rent_payment = models.IntegerField(null=True, blank=True, validators=[validate_gt_0])
    utilities_payment = models.IntegerField(null=True, blank=True, validators=[validate_gt_0])
    point_counter_amount = models.IntegerField(null=True, blank=True, validators=[validate_gt_0])


class Employee(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])
    working_point = models.ForeignKey(TradePoint, on_delete=models.PROTECT)
    salary = models.IntegerField(validators=[validate_gt_0])


class Customer(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])
    info = models.CharField(max_length=255, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])
    description = models.CharField(max_length=255, null=True, blank=True)
    sold_product = models.ManyToManyField(TradePoint, through='SoldProduct',
                                          through_fields=('trade_point', 'product_id'))


class Receipt(models.Model):
    trade_point = models.ForeignKey(TradePoint, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    date = models.DateField()
    receipt_item = models.ManyToManyField(Product, through='ReceiptItem', through_fields=('product_id', 'receipt'))


class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT)
    amount = models.IntegerField(validators=[validate_gt_0])
    price = models.IntegerField(validators=[validate_gt_0])

    class Meta:
        constraints = [
            UniqueConstraint(fields=['receipt', 'product_id'], name='unique_receiptid_productid')
        ]


class SomeStore(models.Model):
    trade_point = models.ForeignKey(TradePoint, on_delete=models.CASCADE)


class DepartmentStore(models.Model):
    trade_point = models.ForeignKey(SomeStore, on_delete=models.CASCADE)


class Store(models.Model):
    trade_point = models.ForeignKey(SomeStore, on_delete=models.CASCADE)


class Section(models.Model):
    trade_point = models.ForeignKey(DepartmentStore, on_delete=models.CASCADE)
    section_number = models.IntegerField(validators=[validate_gt_0])
    section_manager = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    floor = models.IntegerField(validators=[validate_gte_0])

    class Meta:
        constraints = [
            UniqueConstraint(fields=['section_number', 'trade_point'], name='unique_section_number_trade_point')
        ]


class Hall(models.Model):
    trade_point = models.ForeignKey(SomeStore, on_delete=models.CASCADE)
    hall_number = models.IntegerField(validators=[validate_gt_0])
    employees_number = models.IntegerField(null=True, blank=True, validators=[validate_gte_0])

    class Meta:
        constraints = [
            UniqueConstraint(fields=['hall_number', 'trade_point'], name='unique_section_number_trade_point')
        ]


class SoldProduct(models.Model):
    trade_point = models.ForeignKey(TradePoint, on_delete=models.CASCADE, primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[validate_gt_0])
    in_stock = models.IntegerField(validators=[validate_gte_0])

    class Meta:
        constraints = [
            UniqueConstraint(fields=['trade_point', 'product_id'], name='unique_trade_point_id_product_id')
        ]


class Request(models.Model):
    trade_point = models.ForeignKey(TradePoint, on_delete=models.CASCADE)
    date = models.DateField()
    request_item = models.ManyToManyField(Product, through='ReceiptItem', through_fields=('product_id', 'request'))


class RequestItem(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[validate_gt_0])

    class Meta:
        constraints = [
            UniqueConstraint(fields=['request', 'product_id'], name='unique_request_id_product_id')
        ]


class Distributor(models.Model):
    contact = models.CharField(max_length=255, validators=[validate_empty_string])
    rating = models.IntegerField(validators=[validate_gte_0])
    distributor_product = models.ManyToManyField(Product, through='DistributorProduct',
                                                 through_fields=('product_id', 'distributor'))


class DistributorProduct(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[validate_gt_0])
    offer_is_active = models.BooleanField()
    offer_start_date = models.DateField()


class ProductsOrder(models.Model):
    date = models.DateField()
    product_order_item = models.ManyToManyField(DistributorProduct, through='DistributorProduct',
                                                through_fields=('distributor_product_id', 'products_order'))
    request_order = models.ManyToManyField(Request, through='RequestOrder', through_fields=('request', 'order_id'))


class ProductOrderItem(models.Model):
    products_order = models.ForeignKey(ProductsOrder, on_delete=models.CASCADE, primary_key=True)
    distributor_product_id = models.ForeignKey(DistributorProduct, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[validate_gt_0])
    amount = models.IntegerField(validators=[validate_gt_0])

    class Meta:
        constraints = [
            UniqueConstraint(fields=['products_order', 'distributor_product_id'],
                             name='unique_products_order_id_distributor_product_id')
        ]


class RequestOrder(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, primary_key=True)
    order_id = models.ForeignKey(ProductsOrder, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['request', 'order_id'],
                             name='unique_request_id_distributor_order_id')
        ]
