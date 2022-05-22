from django.db import models
from django.db.models import UniqueConstraint

from polls.validators import *


# Create your models here.


class TradePointType(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])

    def __str__(self):
        return self.name


class TradePoint(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])
    point_type = models.ForeignKey(TradePointType, on_delete=models.PROTECT)
    point_size = models.IntegerField(null=True, blank=True, validators=[validate_gt_0])
    rent_payment = models.IntegerField(null=True, blank=True, validators=[validate_gt_0])
    utilities_payment = models.IntegerField(null=True, blank=True, validators=[validate_gt_0])
    point_counter_amount = models.IntegerField(null=True, blank=True, validators=[validate_gt_0])

    def save(self, *args, **kwargs):
        is_save = True
        # execute only on update
        if self.id is not None:
            is_save = False
            old = TradePoint.objects.get(pk=self.id)
            department_store = TradePointType.objects.get(pk=1)
            store = TradePointType.objects.get(pk=2)
            kiosk = TradePointType.objects.get(pk=3)
            tray = TradePointType.objects.get(pk=4)
            if self.point_type != old.point_type:
                # DepartmentStore -> Store
                if old.point_type == department_store and self.point_type == store:
                    DepartmentStore.objects.get(trade_point=SomeStore.objects.get(trade_point=old)).delete()
                # Store -> DepartmentStore
                if old.point_type == store and self.point_type == department_store:
                    DepartmentStore(trade_point=SomeStore.objects.get(trade_point=old)).save()
                # DepartmentStore, Store -> Kiosk, Tray
                if (old.point_type == department_store or old.point_type == store) \
                        and (self.point_type == kiosk or self.point_type == tray):
                    SomeStore.objects.get(trade_point=old).delete()
                # Kiosk, Tray -> Store, DepartmentStore
                if (old.point_type == kiosk or old.point_type == tray) \
                        and (self.point_type == store or self.point_type == department_store):
                    # Kiosk, Tray -> Store
                    s = SomeStore(trade_point=self)
                    s.save()
                    # Kiosk, Tray -> DepartmentStore
                    if self.point_type == department_store:
                        DepartmentStore(trade_point=s).save()
        # execute anyway
        super(TradePoint, self).save(*args, **kwargs)
        # execute only on save
        if is_save and (self.point_type == TradePointType.objects.get(pk=1)
                        or self.point_type == TradePointType.objects.get(pk=2)):
            s = SomeStore(trade_point=self)
            s.save()
            if self.point_type == TradePointType.objects.get(pk=1):
                d = DepartmentStore(trade_point=s)
                d.save()

    def __str__(self):
        return self.name + " | " + self.point_type.__str__()

    def update(self, *args, **kwargs):
        print('update trade point')
        # old = TradePoint.objects.get(pk=self.id)
        # # 1,2 -> 3,4
        # if (old.point_type == TradePointType.objects.get(pk=1) or old.point_type == TradePointType.objects.get(pk=2)) \
        #         and self.point_type != TradePointType.objects.get(pk=1) \
        #         and self.point_type != TradePointType.objects.get(pk=2):
        #     SomeStore.objects.get(pk=self.point_type.id).delete()
        # # 1 -> 1, 2 -> 2
        # # 1 -> 2
        # # 2 -> 1
        # # 3,4 -> 1
        # # 3,4 -> 2
        # # 3,4 -> 3,4
        super(TradePoint, self).update(*args, **kwargs)


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
                                          through_fields=('product_id', 'trade_point'), related_name='sold_products')


class Receipt(models.Model):
    trade_point = models.ForeignKey(TradePoint, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    date = models.DateField()
    receipt_item = models.ManyToManyField(Product, through='ReceiptItem',
                                          through_fields=('receipt', 'product_id'), related_name='receipt_items')


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

    def __str__(self):
        return self.trade_point.__str__()


class DepartmentStore(models.Model):
    trade_point = models.ForeignKey(SomeStore, on_delete=models.CASCADE)

    def __str__(self):
        return self.trade_point.__str__()


# class Store(models.Model):
#    trade_point = models.ForeignKey(SomeStore, on_delete=models.CASCADE)


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
            UniqueConstraint(fields=['hall_number', 'trade_point'], name='unique_hall_number_trade_point')
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
    request_item = models.ManyToManyField(Product, through='RequestItem',
                                          through_fields=('request', 'product_id'), related_name="request_items")


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
    distributor_product = models.ManyToManyField(Product,
                                                 through='DistributorProduct',
                                                 through_fields=('distributor_id', 'product_id'),
                                                 related_name='distributor_products')


class DistributorProduct(models.Model):
    distributor_id = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[validate_gt_0])
    offer_is_active = models.BooleanField()
    offer_start_date = models.DateField()


class ProductsOrder(models.Model):
    date = models.DateField()
    product_order_item = models.ManyToManyField(DistributorProduct, through='ProductOrderItem',
                                                through_fields=('products_order', 'distributor_product_id'),
                                                related_name='product_order_items')
    request_order = models.ManyToManyField(Request, through='RequestOrder', through_fields=('order_id', 'request'),
                                           related_name='request_orders')


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
