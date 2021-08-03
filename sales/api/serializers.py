from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')