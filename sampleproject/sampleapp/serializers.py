from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('department_id','department_name')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('employee_id', 'employee_name', 'department', 
        'date_of_joining', 'photo_file_name')

