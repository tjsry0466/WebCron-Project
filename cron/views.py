# coding: utf-8
import os
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Schedule
from .forms import ScheduleForm
from .helpers import *
    

def Schedule_new(request):
	if request.method == 'POST':
		form = ScheduleForm(request.POST, request.FILES) # NOTE: 인자 순서주의 POST, FILES
		if form.is_valid():
			post = form.save(commit=False) # 중복 DB save를 방지
			post.user = request.user
			post.save()
			return redirect('/crontab')
	else:
		form = ScheduleForm()
	return render(request, 'cron/schedule_new.html',{
		'form': form,
	})

@login_required
def Schedule_delete(request, pk):
    obj = get_object_or_404(Schedule, pk=pk)
    obj.delete()
    return redirect('/crontab/')

def Schedule_detail(request, pk):
    obj = get_object_or_404(Schedule, pk=pk)
    log = os.popen(f"cat /root/venv/WebCron/log/{obj.get_file_name()}.log").read()
    return render(request, 'cron/schedule_detail.html', {'log':log})

def crontab_list(request):
    obj = Schedule.objects.all()
    return render(request, 'cron/crontab_list.html', {'crontab_list':obj})
