# Generated by Django 3.0.4 on 2020-03-20 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cron', '0005_schedule_script'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='fieldir',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='logdir',
        ),
    ]