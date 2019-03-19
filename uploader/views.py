from django.http import HttpResponse
from .models import FileAddress, FileData

def FileUpload(request):

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
