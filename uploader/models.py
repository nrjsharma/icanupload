from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
# import datetime as timezone
from django.utils import timezone


def calculate_delete_date():
    return timezone.now() + timezone.timedelta(days=1)


class FileData(models.Model):
    token = models.CharField(max_length=4, unique=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created.  # NOQA
    delete_date = models.DateTimeField(default=calculate_delete_date)  # NOQA

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
