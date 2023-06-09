#django
from django.contrib.auth import login
#rest_framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
#serializers.py
from .serializers import LoginSerializer
from .serializers import UserSignupSerializer
#models.py
from .models import UserProfileModel

class LoginAPIView(APIView):
    '''
    It is an endpint to login all kinds of users. The user can be either Household User, Driver or Admin
    '''
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)

            # Retrieve UserProfile for the logged-in user
            try:
                profile = UserProfileModel.objects.get(user=user)
                avatar_url = profile.avatar.url if profile.avatar else None
                
                # Return the desired fields in the response
                return Response({
                    'message': 'Login successful',
                    'username': user.username,
                    'firstname': user.first_name,
                    'lastname': user.last_name,
                    'avatar': avatar_url[6:]
                }, status=status.HTTP_200_OK)
            
            except UserProfileModel.DoesNotExist:
                # Handle case where UserProfile does not exist for the user
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

            # generating tokens or setting session data
            # return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
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
