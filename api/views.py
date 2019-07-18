from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from uploader.models import FileData, FileAddress
from api.serializer import (FileAddressSerializer, FileDataSerializers, SignUpUserSerializer)  # NOQA
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny  # NOQA
from django.contrib.auth import get_user_model


class SignUpUserAPIView(CreateAPIView):
    """
    Allow user to signup
    """
    model = get_user_model()
    serializer_class = SignUpUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.POST.get('email', None)
        if not email:
            return Response({'email': ['please provide email']}, status=400)
        elif get_user_model().objects.filter(email=email).exists():
            return Response({'email': ['email already exist']}, status=400)
        else:
            data = request.data
            _serialized = self.serializer_class(data=data)
            if _serialized.is_valid():
                _serialized.save()
                return Response({'data': 'user is created successfully'}, status=201)  # NOQA
            else:
                return Response(_serialized.errors, status=400)


class ShowDownloadAPIView(APIView):
    """
    It will return list of file of the given token from dashboard page
    """
    permission_classes = (AllowAny,)
    http_method_names = ['get', ]

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request):
        _token = request.GET.get('token', None)
        _password = request.GET.get('password', None)
        if _password:
            file_data = get_object_or_404(FileData,
                                          token=_token,
                                          password=_password)
        else:
            file_data = get_object_or_404(FileData, token=_token)

        file_address = FileAddress.objects.filter(token=file_data)
        serializer = FileAddressSerializer(file_address, many=True)
        return Response(serializer.data)


class FileUploadAPIView(APIView):
    """
    This API will upload files from dashboard page
    """
    permission_classes = (AllowAny,)
    http_method_names = ['post', ]

    def post(self, request):
        if request.FILES.get('file', False):
            files = request.FILES.getlist('file')
            file_data = FileData()  # creating a FileData object
            file_data.save()
            for file in files:
                obj = FileAddress(token=file_data, document_name=file.name, document=file)  # NOQA
                obj.save()
            return Response({'data': file_data.token}, status=201)
        else:
            return Response({'data': '404'}, status=404)


class SavePasswordViewSet(ModelViewSet):
    """
    This API will save password if password is provided by the user from dashboard page.  # NOQA
    """
    queryset = FileData.objects.none()
    serializer_class = FileDataSerializers
    permission_classes = (AllowAny,)
    http_method_names = ['patch', ]

    def update(self, request, pk=None, *args, **kwargs):
        token = pk
        file_data = get_object_or_404(FileData, token=token)
        pk = file_data.pk  # NOQA
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