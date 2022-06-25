from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from ..models import MajorBook


def category_IT(request):
    category = 'IT'
    books = MajorBook.objects.all().filter(category='IT').order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})

def category_society(request):
    category = '사회'
    books = MajorBook.objects.all().filter(category='사회').order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})

def category_science(request):
    category = '과학'
    books = MajorBook.objects.all().filter(category='과학').order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})

def category_art(request):
    category = '예술'
    books = MajorBook.objects.all().filter(category='예술').order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})

def category_etc(request):
    category = '기타'
    books = MajorBook.objects.all().filter(category='기타').order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})

