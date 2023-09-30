# rest_framework
from rest_framework import serializers
# models.py
from . import models


class TestImage(serializers.ModelSerializer):
    class Meta:
        model = models.TestImage
        fields = ['name', 'image']


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = models.User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        return user  # super().create(validated_data)


class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfileModel
        fields = '__all__'
