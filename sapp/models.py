
from django.db import models
from datetime import datetime
# Create your models here.
from django.template.backends import django


class StudentInformation(models.Model):
    id_number           = models.IntegerField(blank=False)
    first_name          = models.CharField(max_length=20, blank=True)
    last_name           = models.CharField(max_length=20, blank=True)
    email               = models.EmailField(max_length=50, blank=True)
    phone               = models.CharField(max_length=15, blank=True)
    father_name         = models.CharField(max_length=20, blank=True)
    mother_name         = models.CharField(max_length=20, blank=True)
    department          = models.CharField(max_length=20, blank=True)
    guidancephone      =  models.CharField(max_length=15,blank=True)
    cgpa                = models.CharField(max_length=10, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name


class Answers(models.Model):
    question_1 = models.CharField(max_length=30, blank=False)
    question_2 = models.CharField(max_length=30, blank=False)
    question_3 = models.CharField(max_length=30, blank=False)
    question_4 = models.CharField(max_length=30, blank=False)
    question_5 = models.CharField(max_length=30, blank=False)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question_1

    class Meta:
        verbose_name = 'Answers'
        verbose_name_plural = 'Answers'




class Makequestion(models.Model):
    # ans_name =models.ForeignKey(Questions,on_delete=models.CASCADE)
    # ans_num = models.ForeignKey(Answers,on_delete=models.CASCADE)
    question_title = models.CharField(max_length=500, blank=True)
    mcq_1 = models.CharField(max_length=500, blank=True)
    mcq_2 = models.CharField(max_length=500, blank=True)
    mcq_3 = models.CharField(max_length=500, blank=True)
    mcq_4 = models.CharField(max_length=500, blank=True)
    mcq_5 = models.CharField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.question_title

    class Meta:
        verbose_name = 'Make Questions'
        verbose_name_plural = 'Make Questions'
