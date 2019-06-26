# Api view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.response import Response
from uploader.models import FileData, FileAddress
from .serializer import FileAddressSerializer, FileDataSerializers
from rest_framework.viewsets import ModelViewSet


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
            return Response({'error': 'token not found'}, status=HTTP_404_NOT_FOUND)  # NOQA


class SavePasswordViewSet(ModelViewSet):
    queryset = FileData.objects.none()
    serializer_class = FileDataSerializers

    def update(self, request, pk=None, *args, **kwargs):
        token = pk
        file_data = get_object_or_404(FileData, token=token)
        pk = file_data.pk
        password = request.POST.get('password', '')
        data = {
            'password': password
        }
        _serializer = self.serializer_class(file_data, data)
        if _serializer.is_valid():
            _serializer.save()
            return Response(data=_serializer.data, status=status.HTTP_201_CREATED)  # NOQA
        else:
            return Response(data=_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # NOQA