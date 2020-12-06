# Generated by Django 3.0.5 on 2020-12-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201205_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='doctor_pics'),
        ),
        migrations.AddField(
            model_name='patient',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='patient_pics'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiology', 'Cardiology'), ('Dermatology', 'Dermatology'), ('Pediatrics', 'Pediatrics'), ('Radiology', 'Radiology'), ('Oncology', 'Oncology'), ('Emergency Medicine', 'Emergency Medicine'), ('Gastroenterology', 'Gastroenterology'), ('Allergology/Immunology', 'Allergology/Immunology'), ('Anesthesiology', 'Anesthesiology'), ('Surgeon', 'Surgeon'), ('Dentists', 'Dentists'), ('Ophthalmology', 'Ophthalmology')], default='Cardiologist', max_length=50),
        ),
    ]