from django.db import models
# from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from companies import signals

STATE = (
    ('nj', 'New Jersey'),
    ('wa', 'Washington'),
    ('ny', 'New York'),
)


class ProfileAbstract(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=40, null=True)
    state = models.CharField(max_length=40, choices=STATE)
    country = models.CharField(max_length=40, null=True)
    active = models.BooleanField('active', default=True)

    def clean(self):
        pass

    class Meta:
        abstract = True


# Create your models here.
class Company(ProfileAbstract):

    def __str__(self):
        return self.name


class Employee(ProfileAbstract):
    user = models.ForeignKey(User)
    company = models.ForeignKey(Company, null=False)

    def __str__(self):
        if self.name is None:
            return self.user.username
        else:
            return self.name

# create user before save
pre_save.connect(signals.create_user, sender=Employee)
