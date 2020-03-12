from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length = 200)
    due_date = models.DateTimeField(auto_now = False,blank = True, null = True)
    duration = models.TimeField(blank = True, null = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
