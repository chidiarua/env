from django.shortcuts import render, HttpResponse

# Create your views here.
def HomePage(request):
    return HttpResponse("This is a blog")
