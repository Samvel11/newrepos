from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Patient, Doctor



@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):

    if created:
    	if User == Doctor:

	        Doctor.objects.create(user=instance)
	        print("Profile is Created")
	    else:
	    	Patient.objects.create(user=instance)
        	print("Profile is Created")    
	        


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):

    if created is False:
        instance.profile.save()
        print("updated")
