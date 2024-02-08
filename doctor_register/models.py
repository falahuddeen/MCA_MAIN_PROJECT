from django.db import models

# Create your models here.



class DoctorRegister(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=400)
    profile_pic = models.CharField(max_length=400)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'doctor_register'