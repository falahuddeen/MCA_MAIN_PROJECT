from django.db import models

# Create your models here.


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    feedback = models.CharField(max_length=400)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'feedback'