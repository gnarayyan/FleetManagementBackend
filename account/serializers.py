#django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
#rest
from rest_framework import serializers
from .models import UserProfileModel


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Check if the username and password are valid
        user = authenticate(username=username, password=password)
        if not user:
            print('Invalid username or password.')
            raise serializers.ValidationError('Invalid username or password.')


        # Check if the user is verified
        userprofile = UserProfileModel.objects.get(user=user)
        if userprofile.verification_status != 'V':
            print('User is not verified.')
            raise serializers.ValidationError('User is not verified.')

        data['user'] = user
        return data



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ['avatar']

class SignupSerializer(serializers.Serializer):
    userprofile = UserProfileSerializer(write_only=True, required=False)
    email = serializers.EmailField(source="username")
    class Meta:
        model = User
        fields = ['email', 'password', 'userprofile']

