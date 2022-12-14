from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout, authenticate

# Create your views here.


def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    form = AuthenticationForm()            
    return render(request,'acc/login.html',{'form':form})




def logout_req(request):
    logout(request)
    return redirect('home')

