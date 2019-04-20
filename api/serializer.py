from rest_framework import serializers
from uploader.models import FileAddress


class FileAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileAddress
        fields = ('document', 'document_name')