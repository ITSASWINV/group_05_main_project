from django.db import models
from jobs.models import Jobs
from student.models import Student
# Create your models here.
class Applications(models.Model):
    application_id = models.AutoField(primary_key=True)
    # job_id = models.IntegerField()
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    # student_id = models.IntegerField()
    student =models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'applications'

