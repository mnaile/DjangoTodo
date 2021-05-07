
from re import I
from django.conf import settings
from to_do.settings import SECRET_KEY
from django.contrib.auth.models import User
from todo_app.models import Todo
from rest_framework.response import Response
from rest_framework import status
import jwt


def jwt_decode_handler(token):
    secret_key = SECRET_KEY

    return jwt.decode(
        token, 
        secret_key,
        audience=settings.SIMPLE_JWT.get("AUDIENCE"),
        issuer=settings.SIMPLE_JWT.get("ISSUER"),
        algorithms=[settings.SIMPLE_JWT.get("ALGORITHM")]
        )


def check_token(request, pk=False):
    token = request.headers.get("Authorization").split(" ")[1]
    access_token = jwt_decode_handler(token)

    user = User.objects.filter(email=access_token.get("email")).last()
    if pk:
        todo = Todo.objects.filter(id=pk, user_id=user.id).last()
        return todo
    return user
    