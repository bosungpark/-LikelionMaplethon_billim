from django.shortcuts import render, redirect
from django.contrib import auth
from ..forms import SignupForm
from django.db import transaction
import logging

def signup_view(request):
    """
    회원가입 뷰입니다.
    """
    if request.method == 'POST':
        try:
            with transaction.atomic():
                form = SignupForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    auth.login(request, user)
                    return redirect('mainpage')
                logging.info('Bad Request, status=400')
                return redirect('account:signup')
        except:
            logging.info('ServerError, status=500')
            return redirect('account:signup')

    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
