from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=40)