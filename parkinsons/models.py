from django.db import models

class UploadFileForm(models.Model):
    title = models.CharField(max_length=50)
    file = models.ImageField()