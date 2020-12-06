from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class Patient(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
	age = models.IntegerField(null = True, blank = True )
	phone_number = models.CharField(max_length = 20)
	birth_date = models.DateField(null=True, blank=True)
	email = models.EmailField(max_length = 30, null = True)
	last_name = models.CharField(max_length = 20, null=True)
	first_name = models.CharField(max_length = 20, null=True)
	# user_type = models.CharField(max_length=20, default = 'p')


	# def get_username(self):
    # 	return self.username

    # symptoms = models.CharField(max_length = 100, blank = True)

	#image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

	def __str__(self):
		return str(self.user)

class Doctor(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
	age = models.IntegerField(null = True, blank = True )
	phone_number = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 30, null = True)
	birth_date = models.DateField(null=True, blank=True)
	department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
	last_name = models.CharField(max_length = 20, null=True)
	first_name = models.CharField(max_length = 20, null=True)
	# user_type = models.CharField(max_length=20, default = 'd')

	def __str__(self):
		return str(self.user)

class Messages(models.Model):
	to = models.CharField(max_length = 20, null = True)
	sender = models.CharField(max_length = 20, null = True)
	message = models.CharField(max_length = 20, null=True)

	# def get_username(self):
    # 	return self.username

	#image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

# 	def __str__(self):
# 		return str(self.user.username, self.department)
#
#
# class UserType(models.Model):
#     is_doctor = models.BooleanField(default=False)
#     is_patient = models.BooleanField(default=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         if self.is_patient == True:
#             return User.get_username(self.user) + " - is_patient"
#         else:
#             return User.get_username(self.user) + " - is_doctor"
# #
#
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






# class PatientProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_image = models.ImageField(default='if_elif_else.jpg', upload_to="users")
#     age = models.IntegerField(null=True, blank=True)
#     address = models.TextField(default="my address")
#
#     def __str__(self):
#         return str(self.user.username)
#
#
# class DoctorProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_image = models.ImageField(default='if_elif_else.jpg', upload_to="users")
#     age = models.IntegerField(null=True, blank=True)
#     address = models.TextField(default="my address")
#
#     def __str__(self):
#         return str(self.user.username)
