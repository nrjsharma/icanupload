from django.http import HttpResponse
from .models import FileAddress, FileData
from datetime import datetime, timedelta


def file_upload(request):

    if request.method == 'POST' and request.FILES.get('file', False):
        files = request.FILES.getlist('file')
        file_data = FileData()  # creating a FileData object
        file_data.save()
        for file in files:
            obj = FileAddress(token=file_data,document=file)
            obj.save()
        return HttpResponse(file_data.token)
    else:
        return HttpResponse('else')


def save_password(request):

    if request.method == 'POST':
        token = request.POST.get('token', '')
        password = request.POST.get('password', '')
        delete_after_days = request.POST.get('delete_after', '')
        delete_after = datetime.now() + timedelta(days=int(delete_after_days))
        if password:
            FileData.objects.filter(token=token).update(password=password, delete_date=delete_after)
        return HttpResponse('hello')
