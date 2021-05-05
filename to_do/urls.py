"""to_do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import I
from django.contrib import admin
from django.urls import path, include
from todo_app.views import CreateUserView, LoginView, RefreshTokenView, TodoView, TodoOperationsView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', CreateUserView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh-token/', RefreshTokenView.as_view()),

    # POST, GET all todos
    path('user/todos/', TodoView.as_view()),  
    # GET, DELETE, PUT
    path('user/todo/<int:pk>', TodoOperationsView.as_view())  

]
