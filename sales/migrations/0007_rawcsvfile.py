# Generated by Django 3.2.5 on 2021-07-28 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_order_sales_order_dim_uni_5ced38_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawCsvFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filname', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='sales/raw_file/')),
            ],
        ),
    ]
