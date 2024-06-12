from django.db import models
from student.models import Student
# Create your models here.

class Career(models.Model):
    cr_id = models.AutoField(db_column='Cr_Id', primary_key=True)  # Field name made lowercase.
    st_id = models.IntegerField(db_column='St_Id')  # Field name made lowercase.
    cl_id = models.IntegerField(db_column='Cl_Id')  # Field name made lowercase.
    prediction = models.CharField(db_column='Prediction', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'career'

class Prediction(models.Model):
    prediction_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    career = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'prediction'


