from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import RawCsvFile


@receiver(pre_delete, sender=RawCsvFile)
def delete_file(sender, **kwargs):
    try:
        kwargs['instance'].file.delete()
    except ValueError as ve:
        print(ve)