from django.db import models
from companies.models import Company


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
