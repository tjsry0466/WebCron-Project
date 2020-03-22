# coding: utf-8
import os
import datetime


# linux의 crontab에 있는 cron_list들 추출
def get_crontab_list():
    cron_list = os.popen('./cron_command.sh list').read().strip().split("\n")
    if cron_list==['']:
        return False
    data = []
    for item in cron_list:
        item = item.split()
        data.append([item[1], item[2],item[3],item[4],item[5],item[7],item[9]])
    return data
    

def get_crontab_index(file_dir):
    crontab_list = get_crontab_list()
    if not crontab_list:
        return False
    for (index, item) in enumerate(crontab_list):
        if item[5] == file_dir:
            return index+1 # crontab remove 1 - 1 부터시작
    return False
    

def delete_crontab(filename):
    index = get_crontab_index(filename)
    if index:
        os.system(f'./cron_command.sh remove {index}')
        return True
    return False


