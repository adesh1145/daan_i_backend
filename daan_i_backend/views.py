from django.shortcuts import render
from django.http import HttpResponse


def homePage(request):
    return HttpResponse("<h1>WelCome To Daan-i APP</h1>")
