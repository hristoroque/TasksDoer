from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_date = models.DateField(default = date.today())
    due_date = models.DateField(default = date.today())
    duration = models.TimeField(blank=True,null=True)