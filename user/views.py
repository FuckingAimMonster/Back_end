from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.core import serializers
from .serializers import UserSerializer, SigninSerializer, CheckIdSerializer
from .models import User

class Signup(APIView):
    def post(self, request):
        serializers = UserSerializer(data = request.data)
        if serializers.is_valid():
            User.objects.create(
                username = serializers.data['username'],
                password = serializers.data['password'],
                nickname = serializers.data['nickname'],
                mousedpi = serializers.data['mousedpi'],
                gamedpi = serializers.data['gamedpi'],
                currentdpi = serializers.data['currentdpi'],
            ).save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class Signin(APIView):
    def post(self, request):
        serializer = SigninSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            if User.objects.filter(username = username).exists():
                user = User.objects.get(username = username)
                if serializer.data['password'] == user.password:
                    userjson = serializers.serialize('json', User.objects.filter(username = username))
                    return HttpResponse(userjson, status=200)
        return HttpResponse(status=400)

class Checkid(APIView):
    def post(self, request):
        serializer = CheckIdSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            if User.objects.filter(username = username).exists():
                return HttpResponse(status=401)
            return HttpResponse(status=200)
        return HttpResponse(status=400)

class ModifyDpi(APIView): 
    def post(self, request):
        print(request)
        username = request.data['username']
        if User.objects.filter(username = username).exists():
            user = User.objects.get(username = username)
            user.nickname = request.data['nickname']
            user.gamedpi = request.data['currentdpi']
            user.currentdpi = request.data['currentdpi']
            user.save()
            userjson = serializers.serialize('json', User.objects.filter(username = username))
            return HttpResponse(userjson, status=200)
        return HttpResponse(status=400)
    
class Logout(APIView):
    def post(self, request):
        username = request.data['username']
        if User.objects.filter(username = username).exists():
            return HttpResponse(status=200)
        return HttpResponse(status=400)