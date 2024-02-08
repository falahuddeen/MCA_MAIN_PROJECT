from django.db import models

# Create your models here.


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()
    schedule_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'appointment'
