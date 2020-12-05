from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Patient, Doctor

from .forms import UserForm, PatientRegisterForm, DoctorRegisterForm
from django.contrib.auth.decorators import login_required
import os
# from .models import UserType
# Create your views here.

def register(request):
	return render(request, 'registration/register.html')

def patient_register(request):
	form_user = UserForm()
	form_patient = PatientRegisterForm()

	if request.method =='POST':
		form_user = UserForm(request.POST)
		form_patient = PatientRegisterForm(request.POST)
		if all( [form_user.is_valid(), form_patient.is_valid()]):
			user_p = form_user.save()
			patient = form_patient.save(commit = False)
			patient.user = user_p
			patient.save()
			return render(request, "registration/patient_profile.html")


	context = {'form_user':form_user,
				'form_patient':form_patient
				}

			# username = form.cleaned_data.get('username')
			# password = form.cleaned_data.get('password1')
			# User.objects.create(username = username, password1 = password, password2=password)

			# user = authenticate(request, username = username, password = password)

		# 	if not user is None:
		# 		login(request, user)
		# 	messages.add_message(request, messages.SUCCESS, "User is created successfully")
		# 	return redirect ('patient_profile')
		# else:
		# 	messages.add_message(request, messages.SUCCESS, "User is not created!")

	return render(request, 'registration/patient_registration.html', context)

def doctor_register(request):

	form_user = UserForm()
	form_doctor = DoctorRegisterForm()

	if request.method =='POST':
		form_user = UserForm(request.POST)
		form_doctor = DoctorRegisterForm(request.POST)
		if all( [form_user.is_valid(), form_doctor.is_valid()]):
			user_d = form_user.save()
			doctor = form_doctor.save(commit = False)
			doctor.user = user_d
			doctor.save()
			return render(request, "registration/doctor_profile.html")

	context = {'form_user':form_user,
				'form_doctor':form_doctor
				}

		# 	username = form.cleaned_data.get('username')
		# 	password = form.cleaned_data.get('password1')

		# 	user = authenticate(request, username = username, password = password)

		# 	if not user is None:
		# 		login(request, user)
		# 	messages.add_message(request, messages.SUCCESS, "User is created successfully")
		# 	return redirect ('doctor_profile')
		# else:
		# 	messages.add_message(request, messages.SUCCESS, "User is not created!")

	return render(request, 'registration/doctor_registration.html', context)




def patient_profile(request):
	return render(request, 'registration/patient_profile.html')

def doctor_profile(request):
	return render(request, 'registration/doctor_profile.html')




# def login(request):
#     if (request.method == 'POST'):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
# #
#         if user is not None:
#             login(request, user)
#             type_obj = UserType.objects.get(user=user)
#             if user.is_authenticated and type_obj.is_patient:
#                 return redirect('patient_profile')
#             elif user.is_authenticated and type_obj.is_doctor:
#                 return redirect('doctor_profile')
#         else:
#
#             return redirect('welcome_base')
#
#     return render(request, 'med_app/welcome_base.patient')
#
# def patien_login(request):
#     if request.user.is_authenticated and UserType.objects.get(user=request.user).is_patient:
#         return render(request,'med_app/patient_profile.html)
#     elif request.user.is_authenticated and UserType.objects.get(user=request.user).is_doctor:
#         return redirect('doctor_profile')
#     else:
#         return redirect('login')
#
# def doctor_login(request):
#     if request.user.is_authenticated and UserType.objects.get(user=request.user).is_doctor:
#         return render(request,'med_app/doctor_profile.html)
#     elif request.user.is_authenticated and UserType.objects.get(user=request.user).is_patient:
#         return redirect('patient_profile')
#     else:
#         return redirect('login')








# #####version2
# def login(request,id_):
#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('#')
#         else:
#             messages.info(request, "invalild username or password")
#             return redirect('login')
#     else:
#         return render(request, 'med_app/login.html')






# def login1(request):
#     if (request.method == 'POST'):
#         email = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             type_obj = UserType.objects.get(user=user)
#             if user.is_authenticated and type_obj.is_patient:
#                 return redirect('patient_profile')
#             elif user.is_authenticated and type_obj.is_doctor:
#                 return redirect('doctor_profile')
#         else:
#
#             return redirect('register')
#
#     return render(request, 'med_app/welcome_base.patient')


#
def login_page(request):
    print("#######", request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
	
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        print("########", user)
        if user is not None:
            login(request, user)
            print(user)
            patient = Patient.objects.all().filter(user_id=request.user.id)
            doctor = Doctor.objects.all().filter(user_id = request.user.id)
            if len(patient) != 0:
                return redirect('patient_profile')
            else:
                return redirect('doctor_profile')
    else:
        return render(request, 'registration/login_page.html')
