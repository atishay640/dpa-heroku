from django.db import models
import time
from django.utils.text import slugify

class Order(models.Model):
    uniqueid1= models.CharField(null=True, max_length=150, help_text="Order unique id 1")
    uniqueid2= models.CharField(null=True, max_length=150, help_text="Order unique id 2")
    fact_order_order_key= models.PositiveIntegerField(null=True, help_text="Order key")
    fact_order_Order_Attribute_Key= models.PositiveSmallIntegerField(null=True, help_text="Order attribute key")
    fact_order_Unit_Key= models.PositiveSmallIntegerField(null=True, help_text="Order unit key")
    dim_unit_unit_id= models.PositiveIntegerField(null=True, help_text="Dim Unit unit id")
    fact_order_Order_Date_Key= models.PositiveIntegerField(null=True, help_text="Order order date key")
    fact_order_Order_Time_Key= models.PositiveIntegerField(null=True, help_text="Order order time key")
    fact_order_Register_Key= models.PositiveSmallIntegerField(null=True, help_text="Order register key")
    fact_order_Employee_Key= models.IntegerField(null=True, help_text="Order employee key")
    fact_order_Coupon_Amount= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order coupon amount")
    fact_order_Discount_Amount= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order discount amount")
    fact_order_Net_Food_Sales= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order net food sales")
    fact_order_Net_NonFood_Sales= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order unique id 1")
    fact_order_Giftcard_Sales= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order giftcard sales")
    fact_order_Donations= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order donations")
    fact_order_Taxable_Sales= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order taxable sales")
    fact_order_Tax_Collected= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order tax collected")
    fact_order_Total_Order_Amount= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order total order amount")
    fact_order_Item_Count= models.PositiveSmallIntegerField(null=True, help_text="Order item count")
    fact_order_Order_ID= models.PositiveIntegerField(null=True, help_text="Order id")
    fact_order_Date_Added= models.DateTimeField(null=True, help_text="Order date added") 
    fact_order_Date_Modified= models.DateTimeField(null=True, help_text="Order date modified") 
    fact_order_HashValue= models.TextField(null=True, help_text="Order hash value")
    coupon_id_cnt= models.PositiveIntegerField(null=True, help_text="Coupon id cnt")
    fact_order_Net_Food_Sales1= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order net food sales 1")
    o_startdate= models.PositiveIntegerField(null=True, help_text="Start date")
    o_enddate= models.PositiveIntegerField(null=True, help_text="End date")
    fact_order_DestinationDetail = models.TextField(null=True, help_text='Order Destination detail')
    fact_order_coupon_order_attribute_key = models.PositiveBigIntegerField(null=True, help_text='Order coupon order attribute key')
    fact_order_coupon_order_date_key = models.PositiveIntegerField(null=True, help_text='Order coupon order date key')
    fact_order_coupon_order_time_key = models.PositiveIntegerField(null=True, help_text='Order coupon order time key')
    fact_order_coupon_coupon_key = models.PositiveIntegerField(null=True, help_text='Order coupon key')
    fact_order_coupon_coupon_quantity = models.PositiveIntegerField(null=True, help_text='Order coupon quantity key')
    fact_order_coupon_coupon_amount = models.PositiveIntegerField(null=True, help_text='Order coupon amount key')
    fact_order_coupon_order_id = models.PositiveIntegerField(null=True, help_text='Order coupon order id')
    fact_order_coupon_date_added = models.DateTimeField(null=True, help_text='Order coupon date added')
    fact_order_coupon_date_modified = models.DateTimeField(null=True, help_text='Order coupon date modified')
    dim_coupon_coupon_id = models.PositiveIntegerField(null=True, help_text='Order coupon id')
    dim_coupon_coupon_name = models.CharField(max_length=100, null=True, help_text='Order coupon name')
    new_coupon_amount = models.PositiveIntegerField(null=True, help_text='Order coupon amount')

    class Meta:
       indexes = [
           models.Index(fields=['dim_unit_unit_id', 'dim_coupon_coupon_id',])]
    
    def __str__(self) -> str:
        return self.uniqueid2


class RawCsvFile(models.Model):
    STATUS_CHOICES = (
        (0, 'New'),
        (1, 'InProgress'),
        (2, 'Done'),
    )

    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='csv/')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)


    def save(self, *args, **kwargs):
        if self.file.name:
            self.file.name = f'{slugify(self.filename)}-{round(time.time())}.{self.file.name.split(".")[-1]}'
        super(RawCsvFile, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.filename