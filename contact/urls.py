from django.urls import path
from .views import home_view
from . import views


app_name = 'contact'

urlpatterns = [
    path('', home_view, name='home'),
	path('sidick.html', views.sidick_view, name='sidick'),
	path('register.html', views.register_view, name='register'),
	path('education.html', views.education_view, name='education'),
	path('index1.html', views.index1_view, name='index1'),
	path('Qst3.html', views.Qst3_view, name='Qst3'),
]

