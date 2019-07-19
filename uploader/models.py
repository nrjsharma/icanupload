from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime, timedelta


class FileData(models.Model):
    token = models.CharField(max_length=4, unique=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    upload_date = models.DateTimeField(default=datetime.now())
    delete_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))  # NOQA

    def __str__(self):
        return '%s' % self.token


class FileAddress(models.Model):
    token = models.ForeignKey(FileData, related_name="file_data", on_delete=models.CASCADE)  # NOQA
    document_name = models.TextField()
    document = models.FileField(upload_to='documents/%Y/%m/%d/')

    def __str__(self):
        return '%s' % self.token


@receiver(pre_save, sender=FileData)
def pre_save_file_data(sender, instance=None, created=False, **kwargs):
    from .helper import generate_token
    if instance._state.adding is True:
        # If Creating an object
        print('pre_sav_file_data EXICUTED')
        instance.token = generate_token()
    else:
        # If Updating an object
        pass
