from django.db import models
# Create your models here.




class CareerPath(models.Model):
    career_id = models.AutoField(primary_key=True)
    career = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'career_path'


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    career_id = models.IntegerField()
    alumini_id = models.IntegerField(null=True)
    alumini=models.CharField(max_length=50,null=True)
    student_id = models.IntegerField(null=True)
    student = models.CharField(max_length=50, null=True)
    message = models.CharField(max_length=100)
    sendertype = models.CharField(max_length=50)
    rectype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'chat'
