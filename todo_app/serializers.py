
from django.contrib.auth import models
from django.db.models import fields
from todo_app.models import Todo
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import password_validation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        
        extra_kwargs = {
            'first_name': {'required': True},
            "last_name":{'required': True},
            'username': {'required': True},
            "email":{'required': True},
            "password": {'required': True}} 

    
    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validate_data):
        user = super(UserSerializer, self).create(validate_data)
        user.set_password(validate_data.get('password'))
        user.save()
        return user

class UserDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "username", "last_name", "email"]


class TodoSerializer(serializers.ModelSerializer):
    class Meta:

        model = Todo
        fields = ["id", "user_id", "title", "description"]




    
   
        

