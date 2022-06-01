from django.db import models
from django.db.models import UniqueConstraint

from polls.validators import *


# Create your models here.
# TODO: rename product_id_id in receiptitem, change DateField to DateTimeField, ManyToMany TradePointEmployee
# TODO: нужно пофиксить выбор работников в SectorManager, сделать поле количества работников неактивным,

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


class Employee(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])
    working_point = models.ForeignKey(TradePoint, on_delete=models.PROTECT)
    salary = models.IntegerField(validators=[validate_gt_0])

    def __str__(self):
        return self.name + " | " + str(self.salary) + " | " + self.working_point.name


class Customer(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])
    info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.info is not None:
            return self.name + " | " + self.info
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])
    description = models.CharField(max_length=255, null=True, blank=True)
    sold_product = models.ManyToManyField(TradePoint, through='SoldProduct',
                                          through_fields=('product', 'trade_point'), related_name='sold_products')

    def __str__(self):
        if self.description is not None:
            return self.name + " | " + self.description
        return self.name


class Receipt(models.Model):
    trade_point = models.ForeignKey(TradePoint, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    date = models.DateTimeField()
    receipt_item = models.ManyToManyField(Product, through='ReceiptItem',
                                          through_fields=('receipt', 'product_id'), related_name='receipt_items')

    def __str__(self):
        receipt_items = ReceiptItem.objects.filter(receipt=self)
        total = 0
        for item in receipt_items:
            total += item.price * item.amount

        if self.customer is not None:
            return self.date.__str__() + " | total: " + str(total) + " | " + self.trade_point.name + " | customer: " \
                   + self.customer.name + " | employee: " + self.employee.name
        return self.date.__str__() + " | total: " + str(total) + " | " + self.trade_point.name + " | employee: " + self.employee.name


class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    amount = models.IntegerField(validators=[validate_gt_0])
    price = models.IntegerField(validators=[validate_gt_0])

    class Meta:
        unique_together = (('receipt', 'product'),)

    def __str__(self):
        return str(self.receipt.date) + " | " + self.product.name + " | amount: " + str(self.amount) + " | price: " + str(self.price)


class SomeStore(models.Model):
    trade_point = models.ForeignKey(TradePoint, on_delete=models.CASCADE)

    def __str__(self):
        return self.trade_point.__str__()


class DepartmentStore(models.Model):
    trade_point = models.ForeignKey(SomeStore, on_delete=models.CASCADE)

    def __str__(self):
        return self.trade_point.__str__()


class Section(models.Model):
    trade_point = models.ForeignKey(DepartmentStore, on_delete=models.CASCADE)
    section_number = models.IntegerField(validators=[validate_gt_0])
    section_manager = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    floor = models.IntegerField(validators=[validate_gte_0])

    class Meta:
        unique_together = (('section_number', 'trade_point'),)

    def __str__(self):
        return "section number: " + str(self.section_number) + " | " + self.trade_point.trade_point.trade_point.name + \
               " | manager: " + self.section_manager.name + " | floor: " + str(self.floor)


class Hall(models.Model):
    trade_point = models.ForeignKey(SomeStore, on_delete=models.CASCADE)
    hall_number = models.IntegerField(validators=[validate_gt_0])
    employees_number = models.IntegerField(null=True, blank=True, validators=[validate_gte_0])

    class Meta:
        unique_together = (('hall_number', 'trade_point'),)

    def __str__(self):
        return "hall number: " + str(self.hall_number) + " | " + self.trade_point.trade_point.name + \
               " | employee number: " + str(self.employees_number)


class SoldProduct(models.Model):
    trade_point = models.ForeignKey(TradePoint, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[validate_gt_0])
    in_stock = models.IntegerField(validators=[validate_gte_0])

    class Meta:
        unique_together = (('trade_point', 'product'),)

    def __str__(self):
        return self.trade_point.name + " | " + self.product.name + " | in stock: " + str(self.in_stock) \
               + " | price: " + str(self.price)


class Request(models.Model):
    trade_point = models.ForeignKey(TradePoint, on_delete=models.CASCADE)
    date = models.DateField()
    request_item = models.ManyToManyField(Product, through='RequestItem',
                                          through_fields=('request', 'product'), related_name="request_items")

    def __str__(self):
        return self.trade_point.name + " | " + str(self.date)


class RequestItem(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[validate_gt_0])

    class Meta:
        unique_together = (('request', 'product'),)

    def __str__(self):
        return self.request.__str__() + " | " + self.product.name + " | amount: " + str(self.amount)


class Distributor(models.Model):
    name = models.CharField(max_length=255, validators=[validate_empty_string])
    contact = models.CharField(max_length=255, validators=[validate_empty_string])
    rating = models.IntegerField(validators=[validate_gte_0])
    distributor_product = models.ManyToManyField(Product,
                                                 through='DistributorProduct',
                                                 through_fields=('distributor', 'product'),
                                                 related_name='distributor_products')

    def __str__(self):
        return self.name + " | " + self.contact + " | rating: " + str(self.rating)


class DistributorProduct(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[validate_gt_0])
    offer_start_date = models.DateField()
    offer_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.distributor.name + " | " + self.product.name + " | price: " + str(self.price) +\
               " | " + str(self.offer_start_date) + " | is active: " + (self.offer_end_date is None)


class ProductsOrder(models.Model):
    date = models.DateField()
    product_order_item = models.ManyToManyField(DistributorProduct, through='ProductOrderItem',
                                                through_fields=('products_order', 'distributor_product'),
                                                related_name='product_order_items')
    request_order = models.ManyToManyField(Request, through='RequestOrder', through_fields=('order_id', 'request'),
                                           related_name='request_orders')

    def __str__(self):
        return str(self.date)


class ProductOrderItem(models.Model):
    products_order = models.ForeignKey(ProductsOrder, on_delete=models.CASCADE)
    distributor_product = models.ForeignKey(DistributorProduct, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[validate_gt_0])
    amount = models.IntegerField(validators=[validate_gt_0])

    class Meta:
        unique_together = (('products_order', 'distributor_product'),)

    def __str__(self):
        return "order date: " + str(self.products_order) + " | distributor: " + \
               self.distributor_product.distributor.name + " | " + self.distributor_product.product.name + \
               " | price: " + str(self.price) + " | amount: " + str(self.amount)


class RequestOrder(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    order = models.ForeignKey(ProductsOrder, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('request', 'order'),)

    def __str__(self):
        return self.request.trade_point.name + " | request date: " + str(self.request.date) + " | order date: " + \
               str(self.order.date)
