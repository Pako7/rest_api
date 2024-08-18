from django.db import models

# Create your models here.
class Programmer(models.Model):
  fullname = models.CharField(max_length=100)
  nickname = models.CharField(max_length=50)
  age = models.PositiveSmallIntegerField()
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

class SaleType(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(null=True, blank=True)