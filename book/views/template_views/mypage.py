from django.shortcuts import render, redirect, get_object_or_404
from book.models import MajorBook, BorrowedBook

def mypage(request):
    me = request.user
    books = MajorBook.objects.all().filter(uploader=me).order_by('-id')
    borrowed_books = BorrowedBook.objects.all().filter(borrower=me).order_by('-id')
    return render(request, 'mypage.html', {'books': books,
                                            'borrowed_books':borrowed_books,
                                            })