from django.db import models

# Create your models here.
class Screenshot(models.Model):
    attachment = models.FileField(upload_to='/screenshots/')