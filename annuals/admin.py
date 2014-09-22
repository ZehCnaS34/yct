from django.contrib import admin

# Register your models here.
from annuals.models import ReferenceLink, ContinueEducation, AnnualMeeting
from django.core.mail import send_mail
from django.utils import timezone






def notify_employees(am, company):
    for e in company.employee_set.all():
        print("Sending email to " + e.name + " at " + str(timezone.now()))
        send_mail('Annual meeting', am.title, "arc@asdoifj.com", [e.email], fail_silently=False)



def notify(modeladmin, request, queryset):
    for am in queryset:
        notify_employees(am ,am.company)


class AnnualMeetingView(admin.ModelAdmin):
    actions = [notify]



admin.site.register(ReferenceLink)
admin.site.register(ContinueEducation)
admin.site.register(AnnualMeeting, AnnualMeetingView)
