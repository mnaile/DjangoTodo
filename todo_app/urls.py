from django.urls import path, include
from todo_app.views import CreateUserView, LoginView, RefreshTokenView, TodoView, TodoOperationsView

urlpatterns = [
    
    path('register/', CreateUserView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh-token/', RefreshTokenView.as_view()),
     # POST, GET all todos
    path('user/todos/', TodoView.as_view()),  
    # GET, DELETE, PUT
    path('user/todo/<int:pk>', TodoOperationsView.as_view())  
]
