# Generated by Django 3.2.5 on 2021-07-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid1', models.PositiveBigIntegerField(null=True)),
                ('uniqueid2', models.PositiveIntegerField(null=True)),
                ('fact_order_order_key', models.PositiveIntegerField(null=True)),
                ('fact_order_Order_Attribute_Key', models.PositiveSmallIntegerField(null=True)),
                ('fact_order_Unit_Key', models.PositiveSmallIntegerField(null=True)),
                ('dim_unit_unit_id', models.PositiveIntegerField(null=True)),
                ('fact_order_Order_Date_Key', models.PositiveIntegerField(null=True)),
                ('fact_order_Order_Time_Key', models.PositiveIntegerField(null=True)),
                ('fact_order_Register_Key', models.PositiveSmallIntegerField(null=True)),
                ('fact_order_Employee_Key', models.IntegerField(null=True)),
                ('fact_order_Coupon_Amount', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('fact_order_Discount_Amount', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('fact_order_Net_Food_Sales', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('fact_order_Net_NonFood_Sales', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('fact_order_Giftcard_Sales', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('fact_order_Donations', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('fact_order_Taxable_Sales', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('fact_order_Tax_Collected', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('fact_order_Total_Order_Amount', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('fact_order_Item_Count', models.PositiveSmallIntegerField(null=True)),
                ('fact_order_Order_ID', models.PositiveIntegerField(null=True)),
                ('fact_order_Date_Added', models.DateTimeField(null=True)),
                ('fact_order_Date_Modified', models.DateTimeField(null=True)),
                ('fact_order_HashValue', models.TextField(null=True)),
                ('coupon_id_cnt', models.PositiveIntegerField(null=True)),
                ('fact_order_Net_Food_Sales1', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('o_startdate', models.PositiveIntegerField(null=True)),
                ('o_enddate', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]