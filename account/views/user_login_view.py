from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
import logging


def login_view(request):
    """
    로그인 뷰입니다.
    """
    if request.method=='POST':
        try:
            with transaction.atomic():
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
                        return redirect('mainpage')
                logging.info('Unauthorized, status=401')
                return redirect('account:login')
        except:
            logging.info('ServerError, status=500')
            return redirect('account:login')
    else:
        form=AuthenticationForm()
        return render(request, 'login.html', {'form':form})