import xlsxwriter
from zipfile import ZipFile
from os import path
from django.conf import settings
from django.core.mail import EmailMessage
from datetime import datetime
import jwt


def write_to_xlsxfile(records):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(settings.DPA_REPORT_FILE_PATH)
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1})

    # Adjust the column width.
    worksheet.set_column(1, 1, 15)

    # Write some data headers.
    worksheet.write('A1', 'Store Id', bold)
    worksheet.write('B1', 'Coupon Id', bold)
    worksheet.write('C1', 'Redeem Count', bold)

    # Start from the first cell below the headers.
    row, col = 1, 0

    for store_id, coupon_id, redeem_count in (records):
        worksheet.write_number(row, col,     store_id if store_id else 0)
        worksheet.write_number(row, col + 1, coupon_id if coupon_id else 0)
        worksheet.write_number(
            row, col + 2, redeem_count if redeem_count else 0)
        row += 1
    workbook.close()
    return settings.DPA_REPORT_FILE_PATH


def archive(filepath):
    # Check if file exists
    if path.exists(filepath):
        # get the path to the file in the current directory
        src = path.realpath(filepath)
        # put things into a ZIP archive
        root_dir, tail = path.split(src)
        # more fine-grained control over ZIP files
        with ZipFile(settings.DPA_ZIP_FILE_PATH, "w") as newzip:
            newzip.write(filepath)

        return settings.DPA_ZIP_FILE_PATH
    return None


def send_email_with_file(zip_filepath, email_recipients):
    #
    subject = f"DPA Store Report - {datetime.now().strftime('%B %Y')}"
    payload = {"file" : zip_filepath}
    token = generate_jwt_token(payload)

    message = f""" Hello User, 
    Please find zip file attachement containg coupon redemption report on various Stores.

    Click on the below link to download latest report zip: 
    http://localhost:8000/sales/media/download/{token}

    -Thanks and regards
    DPA Support Team
    """

    email_from = settings.EMAIL_HOST_USER
    email = EmailMessage(subject, message, email_from, email_recipients)
    # email.attach_file(zip_filepath)
    email.send()


def generate_jwt_token(payload:dict):
    return jwt.encode(payload, settings.DPA_JWT_SECRET , algorithm=settings.DPA_JWT_ALGORITHM)

def get_jwt_payload(token):
    return jwt.decode(token, settings.DPA_JWT_SECRET , algorithms=[settings.DPA_JWT_ALGORITHM])
