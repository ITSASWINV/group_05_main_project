from django.db import models
from company.models import Company
from jobs.models import Jobs
# Create your models here.
class Announcement(models.Model):
    announcement_id = models.AutoField(primary_key=True)
    # company_id = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    vacancy = models.CharField(max_length=45)
    # job_id = models.IntegerField()
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'announcement'
