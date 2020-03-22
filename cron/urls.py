from django.urls import path
from . import views


app_name='cron'
urlpatterns = [
        path('new/', views.Schedule_new, name="new"),
        path('delete/<int:pk>/', views.Schedule_delete, name="delete"),
        path('<int:pk>/', views.Schedule_detail, name="detail"),
        path('', views.crontab_list, name="list"),
]
