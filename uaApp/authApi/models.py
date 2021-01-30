from django.db import models
from datetime import datetime


# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

class UserLoginHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    loginAt = models.DateTimeField('Login at')
    
    def __str__(self):
        return str(self.user)+" logged in at "+str(self.loginAt)
        