# Api view
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.response import Response
from uploader.models import FileData, FileAddress
from .serializer import FileAddressSerializer, FileDataSerializers
from rest_framework.viewsets import ModelViewSet
from uploader.models import FileData
from datetime import datetime, timedelta


class ListDownload(APIView):

    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request):
        _token = request.GET.get('token', None)
        _password = request.GET.get('password', None)
        if _password is None or _password == 'null':
            _password = None
        try:
            file_data = FileData.objects.get(token=_token, password=_password)
            file_address = FileAddress.objects.filter(token=file_data)
            serializer = FileAddressSerializer(file_address, many=True)
            return Response(serializer.data)
        except FileData.DoesNotExist:
            return Response({'error': 'token not found'}, status=HTTP_404_NOT_FOUND)


class SavePasswordViewSet(ModelViewSet):
    queryset = FileData.objects.none()
    serializer_class = FileDataSerializers

    def update(self, request, token=None, *args, **kwargs):
        print('-------I AM IN UPDATE---------', token)
        password = request.POST.get('password', '')
        delete_after_days = request.POST.get('delete_after', '')
        delete_after = datetime.now() + timedelta(days=int(delete_after_days))
        print('password', password)
        print('delete_after', delete_after)
        if password:
            print("Password in")
            obj = FileData.objects.get(token=token)
            obj.password = password
            obj.delete_date = delete_after
            obj.save()
        return Response('hello')