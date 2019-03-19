from django.http import HttpResponse
from .models import FileAddress, FileData
from django.views.decorators.csrf import csrf_exempt

def file_upload(request):

    if request.method == 'POST' and request.FILES.get('file', False):
        files = request.FILES.getlist('file')
        file_data = FileData()
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
        if password:
            FileData.objects.filter(token=token).update(password=password)
        return HttpResponse('hello')
