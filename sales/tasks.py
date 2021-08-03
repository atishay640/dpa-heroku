from celery import shared_task
from django.db.models.query import RawQuerySet
from .models import Order, RawCsvFile
from django.conf import settings
import pandas, numpy, time, os, logging
from collections import defaultdict
from django.db.models import Count
from .utils import write_to_xlsxfile, archive, send_email_with_file
from django.contrib.auth.models import User

# Get an instance of a custom logger
logger = logging.getLogger('DPA')

@shared_task
def bulk_insert_from_csv():
    """ The function is used to read csv file in chunks and insert data into database in bulk."""

    if RawCsvFile.objects.filter(status=0).exists() and not RawCsvFile.objects.filter(status=1).exists():
        new_csv_file = RawCsvFile.objects.filter(status=0).last()
        filename = new_csv_file.file.name
    else:
        logger.warning("Either no new csv file available or any existing csv file is in progress.")
        return None

    logger.debug("bulk_insert_from_csv - TRIGGER")
    start_time = time.time()

    # Change file status to In-Progress
    new_csv_file.status = 1
    new_csv_file.save()

    # delete existing table records
    Order.objects.all().delete()
    abs_filename = f'{settings.MEDIA_ROOT}/{filename}'
    dataframe = pandas.read_csv(abs_filename, chunksize=settings.DPA_CSV_FILE_CHUNK_SIZE, iterator=True, encoding='latin1')
    dd = defaultdict(list)

    for chunk in dataframe:
        chunk['fact_order_Date_Added'] = pandas.to_datetime(chunk['fact_order_Date_Added'], utc=True)
        chunk['fact_order_Date_Modified'] = pandas.to_datetime(chunk['fact_order_Date_Modified'], utc=True)
        chunk['fact_order_coupon_date_added'] = pandas.to_datetime(chunk['fact_order_coupon_date_added'], utc=True)
        chunk['fact_order_coupon_date_modified'] = pandas.to_datetime(chunk['fact_order_coupon_date_modified'], utc=True)

        df = chunk.astype(object).replace(numpy.nan, None)
        df = df.where(pandas.notnull(df), None)
        sales_list = df.to_dict('records', into=dd)
        logger.debug("sales_data size = ", len(sales_list))
        orders = [Order(**row) for row in sales_list]

        # Adding chunk records in bulk in Database.
        bulk_insert_in_db(orders)
    
    # Change file status to Done
    new_csv_file.status = 2
    new_csv_file.save()

    logger.debug("Time Taken = %s seconds" % (time.time() - start_time))
    logger.debug("bulk_insert_from_csv - FINISHED")


@shared_task
def bulk_insert_in_db(orders):
    """ Insert sales records in bulk"""

    logger.debug("Inserting records in Database")
    Order.objects.bulk_create(orders)
    logger.debug(f"Record inserted successfully. Last record uniqueid1 = {orders[-1].uniqueid1}")


@shared_task
def generate_report_by_store_and_coupon_monthwise():
    """ Generate coupon redeem report by store id monthwise."""

    logger.debug("generate_report_by_store_and_coupon_monthwise - TRIGGER")
    report_qs = Order.objects.values_list('dim_unit_unit_id', 'dim_coupon_coupon_id') \
    .annotate(redeem_count=Count('dim_unit_unit_id')).order_by('dim_unit_unit_id', '-redeem_count')
    xlsx_filepath = write_to_xlsxfile(list(report_qs))
    logger.debug ("Xlsx file generated on path : ", xlsx_filepath)
    zip_filepath =  archive(xlsx_filepath)
    logger.debug ("Zip file generated on path : ", zip_filepath)
    email_recipients = User.objects.values_list("email")
    send_email_with_file(zip_filepath, email_recipients)
    logger.debug("generate_report_by_store_and_coupon_monthwise - FINISHED")
