from django.db import models
from user_register.models import UserRegister
from doctor_register.models import DoctorRegister
from schedule.models import Schedule

# Create your models here.


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    # schedule_id = models.IntegerField()
    schedule=models.ForeignKey(Schedule,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'appointment'
