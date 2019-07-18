from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from uploader.models import FileAddress, FileData
from django.contrib.auth import get_user_model


class SignUpUserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_staff=False,
            is_superuser=False,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password', 'email', )


class FileAddressSerializer(ModelSerializer):
    class Meta:
        model = FileAddress
        fields = ('document', 'document_name')


class FileDataSerializers(ModelSerializer):
    class Meta:
        model = FileData
        fields = ('password', )
