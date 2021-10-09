from rest_framework import serializers

from .backends import EmailAuthBackend
from .models import Admin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        exclude = ('password', 'created_at', 'updated_at')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'email', 'password', 'name', 'surname')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Admin.objects.create_user(
            **validated_data
        )
        return user


class LoginSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = EmailAuthBackend().authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
