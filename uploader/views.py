from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


def FileUpload(request):

    if request.method == 'POST' and request.FILES.get('file', False):
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print("{}  -  {}".format(filename, uploaded_file_url))
        return HttpResponse('file uploaded succesfuly')
    else:
        return HttpResponse('else')
