from django.shortcuts import render, redirect
from django.contrib import auth
from ..forms import SignupForm
from django.db import transaction
import logging

def signup_view(request):
    """
    공식문서의 설명을 따라 FormView를 상속받아 로직을 단순하게 만들수도 있지만
    restful한 방식을 직접 구현해보고 싶어, 다른 방식으로 구현해보았습니다.
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
