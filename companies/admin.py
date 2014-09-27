from django.contrib import admin

from companies.models import Company, Employee
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
