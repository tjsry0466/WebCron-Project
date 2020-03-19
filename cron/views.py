import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import Schedule


def test(request):
    # a = os.popen('crontab -l').read()
    obj = Schedule.objects.all().first()
    f = open(f'{obj.user.username}_{obj.name}.py', 'w')
    print(obj.script)
    f.write(obj.script)
    f.close()
    return HttpResponse("hello")
