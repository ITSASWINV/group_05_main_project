from django.db import models

# Create your models here.

class TestRound(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_link = models.CharField(max_length=45)
    interview_link = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'test_round'
