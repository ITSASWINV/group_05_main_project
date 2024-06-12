from django.db import models
# from Student.models import Student
#
# # Create your models here.
#
# class Aptitude(models.Model):
#     ap_id = models.AutoField(db_column='Ap_Id',primary_key=True)  # Field name made lowercase.
#     # st_id = models.IntegerField(db_column='St_Id')  # Field name made lowercase.
#     st=models.ForeignKey(Student,to_field='st_id', on_delete=models.CASCADE)
#     date = models.DateField(db_column='Date')  # Field name made lowercase.
#     time = models.TimeField(db_column='Time')  # Field name made lowercase.
#     # pdf = models.CharField(db_column='Pdf', max_length=50)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'aptitude'


from student.models import Student
class Placement(models.Model):
    placement_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    internship = models.IntegerField()
    cgpa = models.IntegerField()
    status = models.CharField(max_length=15)
    backlogs = models.IntegerField()
    stream = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'placement'
