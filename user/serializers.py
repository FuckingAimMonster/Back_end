from rest_framework import serializers
from .models import User, SignIn, CheckId

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'nickname',
            'mousedpi',
            'gamedpi',
            'currentdpi',
        )

class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignIn
        fields = (
            'username',
            'password',
        )

class CheckIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckId
        fields = (
            'username',
        )