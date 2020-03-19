from django.urls import path
from . import views


app_name='cron'
urlpatterns = [
        path('test', views.test),
]
