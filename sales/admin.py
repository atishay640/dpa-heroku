from django.contrib import admin
from .models import Order, RawCsvFile

# Register your models here.

admin.site.register(Order)
admin.site.register(RawCsvFile)
