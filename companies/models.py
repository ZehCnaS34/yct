from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

STATE = (
    ('nj', 'New Jersey'),
    ('wa', 'Washington'),
    ('ny', 'New York'),
)


class AbstractEmployee(models.Model):
    user = models.ForeignKey(User)

    class Meta:
        abstract = True


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
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40, choices=STATE)
    contry = models.CharField(max_length=40)
    active = models.BooleanField('active employee', default=True)

    def clean(self):
        pass

    def __str__(self):
        return self.name
