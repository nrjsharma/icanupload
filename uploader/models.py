from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class FileData(models.Model):
    token = models.CharField(max_length=4, unique=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True) # Automatically set the field to now when the object is first created.

    def __str__(self):
        return '%s - %s ' % (self.token, self.upload_date)


class FileAddress(models.Model):
    token = models.ForeignKey(FileData, related_name="file_data", on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')

    def __str__(self):
        return '%s' % self.token

from .helper import generate_token


@receiver(pre_save, sender=FileData)
def pre_save_token(sender, **kwargs):
    kwargs['instance'].token = generate_token()