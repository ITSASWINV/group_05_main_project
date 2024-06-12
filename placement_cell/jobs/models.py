from django.db import models
from company.models import Company
# Create your models here.
class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    role = models.CharField(max_length=45)
    skills = models.CharField(max_length=45)
    compensation = models.IntegerField()
    location = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    # company_id = models.IntegerField()
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    post_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'jobs'

