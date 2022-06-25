from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=auth.authenticate(
                request=request,
                username=username,
                password=password,
            )

            if user is not None:
                auth.login(request,user)
                return redirect('main')# <임시> 이후 메인으로 수정 필요
        return redirect('account:login')
    else:
        form=AuthenticationForm()
        return render(request, 'login.html', {'form':form})