from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', add, name='add'),
    path('update/<int:todo_id>/', update, name='update'),
    path('delete/<int:todo_id>/', delete, name='delete'),
    path('change/<int:todo_id>/', change, name='change')
]