from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Patient, Doctor

from .forms import UserForm, PatientRegisterForm, DoctorRegisterForm, PatientUpdate, DoctorUpdate
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
			messages.add_message(request, messages.SUCCESS, "Welcome to our app!!")
			return render(request, "registration/patient_profile.html")
		else:
			messages.add_message(request, messages,WARNING, "You are not registered, something went wrong.")

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
			messages.add_message(request, messages.SUCCESS, "Welcome to our app!")
			return render(request, "registration/doctor_profile.html")
		else:
			messages.add_message(request, messages.WARNING, "You are not registered, something went wrong.")
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



def patient_profile(request):
	profile = Patient.objects.get(user_id=request.user.id)
	return render(request, 'registration/patient_profile.html')

def doctor_profile(request):
	profile = Doctor.objects.get(user_id=request.user.id)
	return render(request, 'registration/doctor_profile.html')


def patient_profile_update(request):
	profile = Patient.objects.get(user_id = request.user.id) 

	form = PatientUpdate(instance = profile)

	if request.method == "POST":
		form = PatientUpdate(request.POST, instance = profile)
		if form.is_valid():
			form.save()
			print(request.FILES)
			if request.FILES.get('image', None) != None:
				try:
					os.remove(profile.image.url)
				except Exception as e:
					print('Exception in removing old profile image: ',e)
				profile.image = request.FILES['image']
				profile.save()

			return redirect("patient_profile")
			
	content = {'form':form}
	return render(request, "registration/patient_profile_update.html", content)					



def doctor_profile_update(request):
	profile = Doctor.objects.get(user_id = request.user.id) 

	form = DoctorUpdate(instance = profile)

	if request.method == "POST":
		form = DoctorUpdate(request.POST, instance = profile)
		if form.is_valid():
			form.save()
			print(request.FILES)
			if request.FILES.get('image', None) != None:
				try:
					os.remove(profile.image.url)
				except Exception as e:
					print('Exception in removing old profile image: ',e)
				profile.image = request.FILES['image']
				profile.save()

			return redirect("doctor_profile")
			
	content = {'form':form}
	return render(request, "registration/doctor_profile_update.html", content)		


