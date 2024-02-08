from django.db import models

# Create your models here.



class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()
    sender_type = models.CharField(max_length=20)
    receiver_type = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'chat'