from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User,UserData,UserLoginData

class UserLoginDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLoginData
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

class UserNoPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class UserNoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['type']

