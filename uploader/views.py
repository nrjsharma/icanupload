from django.http import HttpResponse
from .models import FileAddress

def FileUpload(request):

    if request.method == 'POST' and request.FILES.get('file', False):
        files = request.FILES.getlist('file')
        print('files ', files)
        for file in files:
            obj = FileAddress(document=file)
            obj.save()
        return HttpResponse('file uploaded succesfuly')
    else:
        return HttpResponse('else')
