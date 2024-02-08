from django.db import models

# Create your models here.



class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=20)
    disease_symptom = models.CharField(max_length=200)
    disease_image = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'disease'