from django.db import models

class Contact(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  emailaddress = models.CharField(max_length=255)
  comments = models.CharField(max_length=1000)
  checkbox = models.CharField(max_length=1)