from django import forms
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from os import path

from yct.settings import BASE_DIR


from annuals.models import AnnualMeeting

def to_dropdown(model):
    output = ()
    for e in model.objects.all():
        output = output + (e.id, e)
    return tuple([output])


path.join(BASE_DIR, "vault/")


## uploading file
def handle_upload_file(f):
    with open('/home/alex/Desktop/output.txt', 'wb+') as dest:
        for c in f.chunks():
            dest.write(c)


class UploadForm(forms.Form):
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form_text'}))
    file = forms.FileField()
    content = forms.ChoiceField(choices=to_dropdown(AnnualMeeting))


def index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadForm()

    return render(request, 'yct/index.html', {'form': form, 'base': BASE_DIR})
