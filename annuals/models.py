from django.db import models
from companies.models import Company


# Create your models here.
class ReferenceLink(models.Model):
    location = models.CharField(max_length=250)
    display = models.CharField(max_length=250)


    def __str__(self):
        return self.display


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
