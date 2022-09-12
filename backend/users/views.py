from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer

# Create your views here.

class RegisterUser(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Me(APIView):
    serializer_class = UserSerializer
    
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)