# from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages

# from django.contrib.auth.decorators import login_required
# from .forms import UserRegisterForm

# # Create your views here.
# def login_user(request):
#     if request.method=="POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             return redirect('room')
#         else:
#             # Return an 'invalid login' error message.
#             messages.success(request, ("wrong user"))
#             return redirect('login')
#     else:
#         return render(request, 'login.html')


# def register(request):
#     if request.method=="POST":
#         form=UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get('username')
#             messages.success(request,f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form=UserRegisterForm()
#     return render(request,'register.html',{'form':form})




# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import logout
# from django.shortcuts import HttpResponseRedirect
 
# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#         else:
#             return render(request, 'signup.html', {'form': form})
#     else:
#         form = UserCreationForm()
#         return render(request, 'signup.html', {'form': form})
  
# def home(request): 
#     return render(request, 'home.html')
  
 
# def signin(request):
#     print("hello")
#     if request.user.is_authenticated:
#         return render(request, 'home.html')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home.html') #profile
#         else:
#             msg = 'Error Login'
#             form = AuthenticationForm(request.POST)
#             return render(request, 'login.html', {'form': form, 'msg': msg})
#     else:
#         form = AuthenticationForm()
#         return render(request, 'login.html', {'form': form})
 
# def profile(request): 
#     return render(request, 'profile.html')
  
# def signout(request):
#     logout(request)
#     return redirect('/')


from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/"+username+"/")
        else:
            messages.info(request,"invalid credentials")
            
            return redirect("")
    else:
        return render(request,'front.html')


def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                return redirect("login/")
                print('user created')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'reg.html')

def logout(request):
    auth.logout(request)
    return redirect("login")