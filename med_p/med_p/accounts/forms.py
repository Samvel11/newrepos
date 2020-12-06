from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory, ModelForm
from django.contrib.auth.models import User
from .models import Patient, Doctor
from django import forms

# from dobwidget import DateOfBirthWidget

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']


class PatientRegisterForm(ModelForm):
	# birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

	class Meta:
		model = Patient
		fields = '__all__'
		exclude = ['user','age','phone_number','birth_date','image']


CollectionTitleFormSetClient = inlineformset_factory(
    User, Patient, form = PatientRegisterForm,
    fields='__all__', extra = 1, can_delete=True
)



class DoctorRegisterForm(ModelForm):
	# birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

	class Meta:
		model = Doctor
		fields = "__all__"
		exclude = ["user",'age','phone_number','birth_date','department','image']


CollectionTitleFormSetClient = inlineformset_factory(
    User, Doctor, form = DoctorRegisterForm,
    fields='__all__', extra = 1, can_delete=True
)


class PatientUpdate(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ["user"]

class DoctorUpdate(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'  
        exclude = ["user"]      

