# Generated by Django 3.2.5 on 2021-07-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uniqueid1',
            field=models.CharField(max_length=50, null=True),
        ),
    ]