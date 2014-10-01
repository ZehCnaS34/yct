from django.db import models
from companies.models import Company, Employee
from django.db.models.signals import post_save
from django.dispatch import receiver


ANNUAL_TYPES = (
    ('am', 'Annual Meeting'),
    ('ce', 'Continue Education'),
)


class ReferenceLink(models.Model):
    location = models.CharField(max_length=250, null=False)
    display = models.CharField(max_length=250)

    def clean(self):
        pass

    def __str__(self):
        return self.display

    def href(self):
        return "<a href='" + self.location + "'>" + self.display + "</a>"


class AnnualMeeting(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    annual_type = models.CharField(choices=ANNUAL_TYPES,
                                   default='am',
                                   max_length=2)
    year = models.DateTimeField('annual year')
    reference_links = models.ManyToManyField(ReferenceLink)
    response_date = models.DateTimeField('response date', null=True)
    notified_date = models.DateTimeField('notified date', null=True)

    def __str__(self):
        return self.title


class AnnualResponse(models.Model):
    employee = models.ForeignKey(Employee)
    annual_meeting = models.ForeignKey(AnnualMeeting)

    def __str__(self):
        return self.employee + " " + self.annual_meeting


@receiver(post_save, sender=AnnualMeeting)
def create_annual_response(sender, **kwargs):
    employees = sender.company.employee_set

    for e in employees:
        ar = AnnualResponse(employee=e, annual_meeting=sender)
        ar.save()
