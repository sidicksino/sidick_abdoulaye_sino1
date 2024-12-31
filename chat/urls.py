from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:room>/', views.room, name='room'),
    path('checkview/', views.checkview, name='checkview'),
    path('send/', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('message/', views.message_view, name='message_view'),
]
