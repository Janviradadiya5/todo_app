from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    CustomLoginView,
    register,
    index,
    delete_task,
    edit_task,
    complete_task,
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('index/', index, name='index'),

    # Task management
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
]