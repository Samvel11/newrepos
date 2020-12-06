from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views


urlpatterns = [
	path('login_page/', user_views.login_page, name = 'login_page'),
	path('register', user_views.register, name = 'register'),
	path('patient_register/', user_views.patient_register, name = 'patient_register'),
	path('doctor_register/', user_views.doctor_register, name = 'doctor_register'),
	path('doctor_profile/', user_views.doctor_profile, name = 'doctor_profile'),
	path('patient_profile', user_views.patient_profile, name = 'patient_profile'),
	path('chat/<str:user>/', user_views.chat, name = 'chat'),
	path('send_message/<str:user>/', user_views.send_message, name = 'send_message'),
]