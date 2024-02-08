from django.db import models

# Create your models here.



class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()
    review = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'review'