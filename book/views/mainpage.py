from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from ..models import MajorBook, BorrowedBook
from solution.models import Solution#솔루션 책의 데이터

def mainpage(request):
    """
    메인 페이지 함수
    """
    b = MajorBook.objects.all().order_by('-id')
    book_paginator = Paginator(b, 4)
    book = request.GET.get('page')
    books = book_paginator.get_page(book)

    s = Solution.objects.all().order_by('-id')
    solution_paginator = Paginator(s, 4)
    solutions = solution_paginator.get_page(book)

    contents = Solution.objects.all().order_by('-id')
    return render(request, 'mainpage.html', {'books' : books, 'solutions' : solutions,'contents' : contents})