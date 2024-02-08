from django.db import models

# Create your models here.



class UserRegister(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_register'