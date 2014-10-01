from django.contrib import admin

from companies.models import Company, Employee


class EmployeeAdmin(admin.ModelAdmin):
    fields = ['company',
              'name',
              'email',
              'street',
              'city',
              'state',
              'country',
              'active']


# Register your models here.
admin.site.register(Company)
admin.site.register(Employee, EmployeeAdmin)
