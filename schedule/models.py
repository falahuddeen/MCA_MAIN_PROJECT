from django.db import models
from doctor_register.models import DoctorRegister

# Create your models here.


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    # doctor_id = models.IntegerField()
    doctor=models.ForeignKey(DoctorRegister,on_delete=models.CASCADE)
    schedule = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'schedule'
