from django.shortcuts import render

# Create your views here.
def upload(request):
    if request.method == "POST":
        print("Welcome")
    else:
        print("World")
