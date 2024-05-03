from django.db import models

# Create your models here.

class Student(models.Model):
    '''Student Model'''
    student_id = models.BigAutoField(primary_key=True)
    student_name = models.CharField(max_length=500, null=False, blank=False)
    total_marks = models.FloatField(null=True, blank=False)
    
    class Meta:
        db_table = 'student_master'
        managed= True