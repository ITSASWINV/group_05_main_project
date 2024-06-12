from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    semester = models.CharField(max_length=45)
    mail = models.CharField(max_length=45)
    phone = models.IntegerField()
    cgpa = models.CharField(max_length=45)
    skills = models.CharField(max_length=45)
    certificates = models.CharField(max_length=45)
    applied_jobs = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    photo = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    summary = models.CharField(max_length=500)
    ucity = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'student'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student =models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'project'



class Internship(models.Model):
    internship_id =models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student =models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    duration = models.IntegerField()
    company = models.CharField(max_length=45)
    description = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'internship'
