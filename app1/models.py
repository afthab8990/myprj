from django.db import models

class Students(models.Model):
    name = models.TextField(max_length=50)
    rollno = models.IntegerField()

