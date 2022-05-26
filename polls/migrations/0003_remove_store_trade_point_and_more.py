# Generated by Django 4.0.4 on 2022-05-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_customer_departmentstore_distributor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='trade_point',
        ),
        migrations.RemoveConstraint(
            model_name='receiptitem',
            name='unique_receiptid_productid',
        ),
        migrations.RenameField(
            model_name='receiptitem',
            old_name='product_id',
            new_name='product',
        ),
        migrations.AddConstraint(
            model_name='receiptitem',
            constraint=models.UniqueConstraint(fields=('receipt', 'product'), name='unique_receiptid_productid'),
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]