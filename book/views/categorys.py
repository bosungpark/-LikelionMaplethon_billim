from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import MajorBook


def category(request):
    """
    카테고리 선택 함수입니다.
    """
    category = request.get("category","")
    books = MajorBook.objects.all().filter(category=category).order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})