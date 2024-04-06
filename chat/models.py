from django.db import models

# Create your models here.

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100)
    doctor_id = models.IntegerField()
    user_id = models.IntegerField()
    sendertype = models.CharField(max_length=20)
    rectype = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'chat'




