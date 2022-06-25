from django.shortcuts import render, redirect
from django.contrib import auth

def logout_view(request):
    auth.logout(request)
    return redirect('main')# <임시> 이후 메인으로 수정 필요