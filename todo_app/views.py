from functools import partial
from os import access, stat
from re import I
from todo_app.models import Todo
from todo_app.utils import check_token, jwt_decode_handler
from django.shortcuts import render
from todo_app.serializers import TodoSerializer, UserSerializer, UserDetail
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User



# Create your views here.


class CreateUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            data = dict(serializer.data)
            data.pop("password")
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)

        data = data.data

        access_token = jwt_decode_handler(data.get("access"))
        user = User.objects.filter(username=access_token.get("username")).last()
        if not user:
            return Response({"error":True, "message":"No such a user"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserDetail(user)

        todos =  Todo.objects.filter(user_id=user.id).all()
        todos = TodoSerializer(todos, many=True).data

        data["user"] = serializer.data
        data["todos"] = todos
        return Response(data)


class RefreshTokenView(TokenRefreshView):

    def post(self, request, *args, **kwargs):

        data = super().post(request, *args, **kwargs)
        data = data.data

        return Response(data)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = check_token(request)
        user_data = UserDetail(user).data
        return Response({"user": user_data})


        


class TodoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        user = check_token(request)
        
        data["user_id"] = user.id
        serializer = TodoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):

        user = check_token(request)

        todos = Todo.objects.filter(user_id=user.id).all()
        if not todos:
            return Response({"error": True, "message": "No such todos"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TodoSerializer(todos, many=True).data

        return Response(serializer)


class TodoOperationsView(APIView):

    def get(self, request, pk):
 
        todo = check_token(request, pk)
        if not todo:
            return Response({"error": True, "message": "No such a user or todo"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo).data
        return Response(serializer)

    
    def delete(self, request, pk):
        
        todo = check_token(request, pk)
        if not todo:
            return Response({"error": True, "message": "No such a user or todo"}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response({"status": "OK", "message": "Todo has been deleted"})

    
    def put(self, request, pk):

        todo = check_token(request, pk)
        if not todo:
            return Response({"error": True, "message": "No such a user or todo"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(instance=todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        

        



