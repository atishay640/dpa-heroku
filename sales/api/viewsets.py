from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from sales.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    @action(detail=False, methods=['GET'])
    def check_email(self, request): 
        if request.query_params.get("email"):
            is_exist = self.get_queryset().filter(email=request.query_params.get("email")).exists()
            return Response({"is_exist": is_exist})
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def check_username(self, request):
        if request.query_params.get("username"):
            is_exist = self.get_queryset().filter(username=request.query_params.get("username")).exists()
            return Response({"is_exist": is_exist})
        return Response(status=status.HTTP_400_BAD_REQUEST)
