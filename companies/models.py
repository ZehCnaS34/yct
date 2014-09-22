from django.db import models
from django.core.exceptions import ValidationError

STATE = (
    ('nj', 'New Jersey'),
    ('wa', 'Washington'),
    ('ny', 'New York')
)


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40, choices=STATE)
    contry = models.CharField(max_length=40)


    active = models.BooleanField('active company', default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40, choices=STATE)
    contry = models.CharField(max_length=40)


    active = models.BooleanField('active employee', default=True)

    def __str__(self):
        return self.name