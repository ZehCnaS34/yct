from django.shortcuts import render

# Create your views here.

from annuals.models import AnnualMeeting, ContinueEducation


def index(request):
    ams = AnnualMeeting.objects.all()
    ces = ContinueEducation.objects.all()

    return render(request, 'annuals/index.html', {
        'ams': ams,
        'ces': ces,
    })


def sign(request, annual_id, annual_type):
    ann = None
    if annual_type == 'am':
        ann = AnnualMeeting.objects.get(pk=annual_id)

    elif annual_type == 'ce':
        ann = ContinueEducation.objects.get(pk=annual_id)

    return render(request, 'annuals/sign.html', {'ann': ann})
