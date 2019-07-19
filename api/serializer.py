from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer, Serializer
from uploader.models import FileAddress, FileData
from django.contrib.auth import get_user_model, authenticate


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


class LoginSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, validated_data):
        username = validated_data.get('username', '')
        password = validated_data.get('password', '')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    validated_data['user'] = user
                else:
                    raise exceptions.ValidationError(detail='user is deactivated')  # NOQA
            else:
                raise exceptions.NotFound(detail='user not found')
        else:
            raise exceptions.ValidationError(detail='username or password is not provided')  # NOQA
        return validated_data


class FileAddressSerializer(ModelSerializer):
    class Meta:
        model = FileAddress
        fields = ('document', 'document_name')


class FileDataSerializers(ModelSerializer):
    class Meta:
        model = FileData
        fields = ('password', )
