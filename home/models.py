from django.db import models

# Create your models here.
class student(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    f_name=models.CharField(max_length=50,null=True)
    l_name=models.CharField(max_length=40,null=True)
    email=models.EmailField(null=True)
