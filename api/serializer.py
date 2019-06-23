from rest_framework.serializers import ModelSerializer
from uploader.models import FileAddress, FileData


class FileAddressSerializer(ModelSerializer):
    class Meta:
        model = FileAddress
        fields = ('document', 'document_name')


class FileDataSerializers(ModelSerializer):
    class Meta:
        model = FileData
        fields = '__all__'
