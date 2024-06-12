from django.db import models
from chat.models import CareerPath
# Create your models here.
class Alumini(models.Model):
    alumini_id = models.AutoField(db_column='alumini__id', primary_key=True)  # Field renamed because it contained more than one '_' in a row.
    name = models.CharField(max_length=45)
    mail = models.CharField(max_length=45)
    phone = models.IntegerField()
    career = models.ForeignKey(CareerPath,on_delete=models.CASCADE)
    experience = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    year=models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alumini'
