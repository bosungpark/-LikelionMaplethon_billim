from django.shortcuts import render, redirect
from django.contrib import auth
from ..forms import SignupForm
from django.contrib.auth.forms import UserChangeForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)

            user = UserChangeForm(instance=request.user).save(commit=False)
            user.coin = 2
            user.save()
            return redirect('main')

        return redirect('account:signup')

    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
