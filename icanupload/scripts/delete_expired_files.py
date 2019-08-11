"""
    This script will delete all the files whose delete_date is less then today
"""
from uploader.models import FileData
from django.utils import timezone


def delete_files():
    files = FileData.objects.filter(delete_date__lt=timezone.now())
    files_count = files.count()
    files.delete()
    print(files_count, 'file deleted')


if __name__ == '__main__':
    delete_files()
