from django.shortcuts import render
from django.http import HttpResponse
import os

def test(request):
    a = os.popen('crontab -l').read()
    return HttpResponse(a)
