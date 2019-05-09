from django.shortcuts import render
from .models import Employee, License
# Create your views here.

def index(request):
    employee_list = Employee.objects.all()
    license_list = License.objects.all()


    context = {
        'employee_list': employee_list,
        'license_list': license_list,
    }

    return render(request, 'remindme/index.html', context)