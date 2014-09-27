from django.db import models
from companies.models import Company, Employee


# Create your models here.
class ReferenceLink(models.Model):
    location = models.CharField(max_length=250)
    display = models.CharField(max_length=250)

    def __str__(self):
        return self.display

    def href(self):
        return "<a href='" + self.location + "'>" + self.display + "</a>"


class AnnualMeeting(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    year = models.DateTimeField('annual year')
    reference_links = models.ManyToManyField(ReferenceLink)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.title


class ContinueEducation(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    year = models.DateTimeField('annual year')
    reference_links = models.ManyToManyField(ReferenceLink)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.title


class AnnualMeetingResponse(models.Model):
    annual_meeting = models.ForeignKey(AnnualMeeting)
    employee = models.ForeignKey(Employee)
    response_date = models.DateTimeField('reponse date')

    def __str__(self):
        return self.annual_meeting + " " + self.employee


class ContinueEducationResponse(models.Model):
    continue_education = models.ForeignKey(ContinueEducation)
    employee = models.ForeignKey(Employee)
    response_date = models.DateTimeField('reponse date')

    def __str__(self):
        return self.continue_education + " " + self.employee
