from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    n = models.CharField(max_length=100)
    c = models.IntegerField()


class Enrollment(models.Model):
    u = models.ForeignKey(User, on_delete=models.CASCADE)
    c = models.ForeignKey(Course, on_delete=models.CASCADE)
    g = models.CharField(max_length=5)
    d = models.DateField(auto_now_add=True)
