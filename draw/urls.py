# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image_board', views.image_board, name="image_board"),
    path('<str:room_name>/', views.room, name='room')
]
