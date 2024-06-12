from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    about = models.CharField(max_length=45)
    mail = models.CharField(max_length=45)
    phone = models.IntegerField()
    status = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'company'

