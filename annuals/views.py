from django.shortcuts import render

# Create your views here.

from annuals.models import AnnualMeeting


def index(request):

    ams = AnnualMeeting.objects.all()

    return render(request, 'annuals/index.html', {'ams': ams})
