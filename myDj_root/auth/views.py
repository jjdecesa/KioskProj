from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authLogin, logout as authlogout

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        
        authLogin(request, myuser)
         
        return redirect('myapp:home')

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            authLogin(request, user)
            return redirect('myapp:home')


    return render(request, 'login.html')

def logout(request):
    authlogout(request)
    return redirect('myapp:home')



# Create your views here.
