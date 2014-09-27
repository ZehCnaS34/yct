from django import forms
from django.shortcuts import  render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from forms.models import Form



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


def index(request):
    forms = Form.objects.all()
    form = LoginForm()
    return render(request, 'yct/index.html', {'form': form, 'forms': forms})
