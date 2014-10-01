from django.contrib import admin

# Register your models here.
from annuals.models import ReferenceLink, AnnualMeeting

# notifies employees
admin.site.register(ReferenceLink)
admin.site.register(AnnualMeeting)
