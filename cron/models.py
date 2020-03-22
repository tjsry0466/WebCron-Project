import os
from django.db import models
from django.conf import settings
from .helpers import get_crontab_list, delete_crontab
from .behaviors import TimeStampMixin
from .contstans import CYCLE_CHOICES


class Schedule(TimeStampMixin, models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    script = models.TextField()
    # fieldir = models.CharField(max_length=100)
    # logdir = models.CharField(max_length=100)
    cycle = models.CharField(max_length=10, choices=CYCLE_CHOICES)
    minute =  models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    week = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    dayoftheweek = models.CharField(max_length=2)

    def get_file_name(self, *args, **kwargs):
        super(Schedule, self).save(*args, **kwargs)
        now_time = "_".join(self.created_at.strftime('%Y-%m-%d %H:%M:%S').split())
        filename = f'{self.user.username}_{self.name}_{now_time}.py'
        return filename

    def create_file(self):
        filename = self.get_file_name()
        try:
            f = open(filename , 'w')
            f.write(self.script)
            f.close()
            return filename
        except Exception as e:
            print(e)
        return False

    def is_unique(self):
        crontab_list = get_crontab_list()
        crontab_item = []
        filename = self.get_file_name()
        if crontab_list:
            crontab_item = [item for item in crontab_list if filename in item[5]]
        
        if not crontab_item:
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        if self.cycle == "DA":
            self.minute = '*'
            self.day = 1
            self.week = '*'
            self.month = '*'
            self.dayoftheweek = '*'
        if self.cycle == "MI":
            self.minute = '*'
            self.day = '*'
            self.week = '*'
            self.month = '*'
            self.dayoftheweek = '*'

        if not self.is_unique():
            return False

        filename = self.create_file()
        if not filename:
            return False

        os.system(f'mv {self.get_file_name()} ./excute_data')
        os.system(f'./cron_command.sh add "{self.minute} {self.day} {self.week} {self.month} {self.dayoftheweek} /usr/bin/python3.6 /root/venv/WebCron/excute_data/{self.get_file_name()} >> /root/venv/WebCron/log/{self.get_file_name()}.log"')          
        super(Schedule, self).save(*args, **kwargs)

    def delete(self):
        file_dir = f'/root/venv/WebCron/excute_data/{self.get_file_name()}'
        if delete_crontab(file_dir):
            os.system(f'rm -rf {file_dir}')          
        # os.system(f'rm -rf /root/venv/WebCron/log/{self.get_file_name()}.log') # 로그는 지우지말자,,
            super(Schedule, self).delete()