from django.shortcuts import render

# Create your views here.

from annuals.models import AnnualMeeting


def index(request):
    ams = AnnualMeeting.objects.all()

    return render(request, 'annuals/index.html', {
        'ams': ams,
    })


def sign(request, annual_id, annual_type):
    ann = AnnualMeeting.objects.get(pk=annual_id)


    return render(request, 'annuals/sign.html', {'ann': ann})
