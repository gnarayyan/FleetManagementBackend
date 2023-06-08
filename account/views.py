#django
from django.contrib.auth import login
#rest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
#other
from .serializers import LoginSerializer


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


        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']
        # login(request, user)
        # return Response({'message': 'Login successful'}, status=status.HTTP_202_ACCEPTED)
       