from django.shortcuts import render
from django.http import HttpResponse  # NOQA
from django.views import View
from uploader.models import FileData


class DashboardView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'dashboard/dashboard/dashboard.html')
        else:
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
                return render(request, 'dashboard/index/index.html', context)
            else:
                return render(request, 'dashboard/index/index.html')
