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
	path('doctor_profile_update/', user_views.doctor_profile_update, name = 'doctor_profile_update'),
	path('patient_profile_update', user_views.patient_profile_update, name = 'patient_profile_update'),
	]
