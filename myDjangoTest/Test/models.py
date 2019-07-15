from django.db import models

# ORM 框架使用
# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
