#django
from django.contrib.auth import login
#rest_framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

#serializers.py
from .serializers import LoginSerializer
from .serializers import UserSignupSerializer

class LoginAPIView(APIView):
    '''
    It is an endpint to login all kinds of users. The user can be either Household User, Driver or Admin
    '''
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            # generating tokens or setting session data
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignupAPIView(APIView):
    '''
    It is an endpoint to signup household users. The user can signup but will be activated only after the admin verifies it.
    '''
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User signup successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
