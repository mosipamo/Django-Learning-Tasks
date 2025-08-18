from django.urls import path
from .views import signup, loginn, todo, edit_todo, delete_todo, signout

urlpatterns = [
    path('', signup, name="signup-page"),
    path('login/', loginn, name="login-page"),
    path('todo-page/', todo, name="todo-page"),
    path('edit-todo/<int:srno>', edit_todo, name="edit-todo"),
    path('delete-todo/<int:srno>', delete_todo, name="delete-todo"),
    path('signout/', signout, name="signout-page")
]
