#django
from django.contrib.auth import authenticate,get_user_model
#rest_framework
from rest_framework import serializers
#models.py
from .models import UserProfileModel



User = get_user_model()

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


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    avatar = serializers.ImageField(write_only=True, required=False)
    userprofile = UserProfileSerializer(write_only=True, required=False)

    def create(self, validated_data):
        avatar = validated_data.pop('avatar', None)
        userprofile_data = validated_data.pop('userprofile', {})
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['firstname'],
            last_name=validated_data['lastname']
        )

        if avatar:
            UserProfileModel.objects.create(user=user, avatar=avatar)

        if userprofile_data:
            UserProfileModel.objects.create(user=user, **userprofile_data)

        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'firstname', 'lastname', 'avatar', 'userprofile']
