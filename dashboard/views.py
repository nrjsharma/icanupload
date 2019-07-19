from django.shortcuts import render
from django.http import HttpResponse
from uploader.models import FileData
# Create your views here.


def home(request):
    if request.method == "GET":
        token_id = request.GET.get('s', '')
        if token_id:
            try:
                file = FileData.objects.get(token=token_id)
                if file.password:
                    context = {
                        'data': file.password,
                        'key': token_id
                    }
                else:
                    context = {
                        'data': 'Download',
                        'key': token_id
                    }
            except FileData.DoesNotExist:
                context = {
                    'data': "Wrong",
                    'key': token_id
                }
            return render(request, 'dashboard/home.html', context)
        else:
            return render(request, 'dashboard/home.html')
    else:
        return HttpResponse("POST")
