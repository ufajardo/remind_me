"""

check_status() -- This will be the function that the cronjob prompts and will go through all of
    license expiration dates and check for 90, 60, 30 days for when the license expires.

send_email() -- A separate function that will be dedicated to emailing the email listed on the
    employee's account.

Resource: https://simpleisbetterthancomplex.com/tutorial/2016/06/13/how-to-send-email.html
https://realpython.com/asynchronous-tasks-with-django-and-celery/


"""
from remindme.models import Employee, License
from django.core.mail import send_mail
import datetime

def check_status():
    license = License.objects.all()

    for lic in license:
        if lic.expiration == lic.expiration - datetime.timedelta(days=30):
            emp = Employee.objects.get(id=lic.employee.id)
            send_mail(
                '30 days until your license expires!',
                '30 days until your license expires!',
                'some_email@gmail.com',
                [emp.email],
                fail_silently=False,
            )

