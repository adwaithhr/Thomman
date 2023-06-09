from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages


def login(request):
    if request.method == "POST":
        # print("in login post"+request.method)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/"+username+"/profile/")
        else:
            messages.info(request, "invalid credentials")
            # print("incorrect")
            return redirect('/')
    else:
        return render(request, 'front.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                print("useranme")
                return render(request, 'reg.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                print("email")
                return render(request, 'reg.html')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                print("correct")
                return redirect('/')
        else:
            messages.info(request, 'password not matching')
            print("password")
            return render(request, 'reg.html')
    else:
        return render(request, 'reg.html')


def logout_view(request):
    auth.logout(request)
    return redirect("login")
