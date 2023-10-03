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


class UserProfileForSchedule(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')

    class Meta:
        model = models.UserProfileModel
        fields = ('user', 'avatar', 'full_name')

    def get_full_name(self, obj):
        # user = models.User.objects.get(id=obj.user)
        return obj.user.get_full_name()

# class UserProfileForSchedule(serializers.Serializer):
#     user_id = serializers.IntegerField(source='user')
#     user_full_name = serializers.CharField(source='user.get_full_name')
#     image_url = serializers.SerializerMethodField()

#     def get_image_url(self, obj):
#         if obj.avatar:
#             return self.context['request'].build_absolute_uri(obj.avatar.url)
#         return None
