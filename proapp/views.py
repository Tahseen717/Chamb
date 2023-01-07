from django.shortcuts import render,redirect
from .models import product
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'GET':
        nafi = request.GET.get ('query')
        if nafi:
            n  = product.objects.filter(name__icontains=nafi)
            return render(request, 'index.html', locals())
        
    return render(request, "index.html")

def login (request):
    if request.method == 'POST':
        usernm = request.POST ['username']
        password = request.POST ['password']
        user = auth.authenticate(username=usernm, password= password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'User log in success')
            return render(request, 'index.html')
        else:
            messages.warning(request, 'User Not Found, Please register your account')
            return render(request, 'reg_istration.html')

    return render(request, "login.html")

def reg (request):

    if request.method == "POST":
        
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'This User already exist')
                return redirect('/reg')
            else:
                user = User.objects.create_user(email=email,username=username, password=password1).save()
                messages.success(request, 'Welcome')
                return redirect('login')

    return render(request, "reg.html")



