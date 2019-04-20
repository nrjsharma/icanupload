# Api view
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.response import Response
from uploader.models import FileData, FileAddress
from .serializer import FileAddressSerializer


class ListDownload(APIView):

    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        _token = request.GET.get('token', None)
        _password = request.GET.get('password', None)
        print('token', _token)
        print('password', _password)
        if _password is None or _password == 'null':
            _password = None
        try:
            file_data = FileData.objects.get(token=_token, password=_password)
            file_address = FileAddress.objects.filter(token=file_data)
            serializer = FileAddressSerializer(file_address, many=True)
            return Response(serializer.data)
        except FileData.DoesNotExist:
            return Response({'error': 'token not found'}, status=HTTP_404_NOT_FOUND)
