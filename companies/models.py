from django.db import models
# from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

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

    class Meta:
        abstract = True


# Create your models here.
class Company(ProfileAbstract):

    def __str__(self):
        return self.name


class Employee(ProfileAbstract):
    user = models.ForeignKey(User)
    company = models.ForeignKey(Company, null=True)

    def clean(self):
        pass

    def __str__(self):
        if self.name is None:
            return self.user.username
        else:
            return self.name


def create_user(sender, **kwargs):
    password = User.objects.make_random_password()
    e = kwargs['instance']
    fn, ln = e.name.split(' ')
    uname = e.name + e.company.name
    user = User(username=uname,
                password=password,
                first_name=fn,
                last_name=ln,
                email=e.email)
    user.save()
    e.user_id = user.id

# create user before save
pre_save.connect(create_user, sender=Employee)
