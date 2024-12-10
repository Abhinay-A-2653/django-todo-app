from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
