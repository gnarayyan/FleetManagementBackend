# django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

# JWT Auth
from rest_framework_simplejwt.tokens import RefreshToken

# models & serializers
from . import serializers
from . import models


class TestImage(viewsets.ModelViewSet):
    serializer_class = serializers.TestImage
    queryset = models.TestImage.objects.all()


class UserProfile(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfile
    queryset = models.UserProfileModel.objects.all()
    # permission_classes = [IsAuthenticated]

    # @action(detail=True, methods=['GET'])
    # def user_profile_by_id(self, request, pk=None):
    #     userprofile = get_object_or_404(self.queryset, user__id=pk)
    #     serializer = self.get_serializer(userprofile)
    #     return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = models.UserProfileModel.objects.filter(user__id=pk)
        userprofile = get_object_or_404(queryset, user__id=pk)
        serializer = serializers.UserProfile(userprofile)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = models.UserProfileModel.objects.all()
    #     userprofile = get_object_or_404(queryset, pk=pk)
    #     serializer = serializers.UserProfile(userprofile)
    #     return Response(serializer.data)


class SignupAPIView(APIView):
    '''
    It is an endpoint to signup users. The user can signup but will be activated only after the admin verifies it.
    '''

    def post(self, request):
        serializer = serializers.RegisterUserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # print('DATA: ', serializer._validated_data)
            user = serializer.create(serializer._validated_data)
            return Response(
                {'message': 'User signup successful', 'id': user.id}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    '''
    It is an endpint to login all kinds of users. The user can be either Household User, Driver or Admin.
    After each successful login user gets tokens
    '''

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(
                {
                    'fullname': user.get_full_name(),
                    'email': user.email,
                    'id': user.pk,
                    'username': user.get_username(),
                    'tokens': tokens,
                    'role': models.UserProfileModel.objects.get(user=user).role
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {'error': 'Invalid username or password'},
            status=status.HTTP_400_BAD_REQUEST,
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserProfileForSchedule(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.UserProfileForSchedule

    def get_queryset(self):
        role = self.request.query_params.get('role', None)
        if role is not None:
            return models.UserProfileModel.objects.filter(role=role)
        return models.UserProfileModel.objects.all()


# class UserProfileForSchedule(viewsets.ReadOnlyModelViewSet):
#     serializer_class = serializers.UserProfileForSchedule

#     def get_queryset(self):
#         role = self.request.query_params.get('role')
#         return models.UserProfileModel.objects.filter(role=role)
