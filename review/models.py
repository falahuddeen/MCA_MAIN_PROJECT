from django.db import models
from user_register.models import UserRegister
from doctor_register.models import DoctorRegister

# Create your models here.



class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    # doctor_id = models.IntegerField()
    doctor=models.ForeignKey(DoctorRegister,on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'review'