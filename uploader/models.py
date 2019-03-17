from django.db import models

class FileAddress(models.Model):
    token = models.IntegerField(default=1,null=True,blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')