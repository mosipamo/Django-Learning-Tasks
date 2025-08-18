from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        user = User.objects.create_user(fnm, emailid, pwd)
        user.save()
        return redirect('/login')
        
    return render(request=request, template_name="signup.html", context={})

def loginn(request):
    if request.method == "POST":
        fnm = request.POST.get("fnm")
        pwd = request.POST.get("pwd")
        user = authenticate(request=request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/todo-page')
        else:
            return redirect('/login')
            
        
    return render(request=request, template_name="login.html", context={})

@login_required(login_url='/login')
def todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        user = request.user
        obj = Todo(title=title, user=user)
        obj.save()
        
        res = Todo.objects.filter(user=user).order_by('-date')
        return redirect('/todo-page', {'res': res})
    user = request.user
    res = Todo.objects.filter(user=user).order_by('-date')
    return render(request=request, template_name="todo.html", context={"res": res})

@login_required(login_url='/login')
def edit_todo(request, srno):
    if request.method == "POST":
        title = request.POST.get("title")
        obj = Todo.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todo-page')
    
    obj = Todo.objects.get(srno=srno)
    return render(request=request, template_name="edit_todo.html", context={'obj': obj})

@login_required(login_url='/login')
def delete_todo(request, srno):
    obj = Todo.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo-page')

def signout(request):
    logout(request)
    return redirect('/login')