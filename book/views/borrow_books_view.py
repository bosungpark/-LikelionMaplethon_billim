from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from ..models import MajorBook, BorrowedBook
from ..forms import BorrowedBookForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm

def book_list(request):
    """
    책 대여하기 함수
    """
    books = MajorBook.objects.all().order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts})

def rental(request, id):
    """
    책 빌리기 기능 함수
    """
    rental_book = MajorBook.objects.get(pk=id)
    rental_status=rental_book.status #대여여부
    
    if rental_status == '대여 가능':
        user=UserChangeForm(instance = request.user).save(commit=False)#대여시 빌린이의 코인을 차감해줍니다
        if user.coin:
            if user.coin>0:#코인이 1개 이상일 때만, 대출이 가능합니다.
                if rental_book.uploader != user: #자신이 올린 책을 스스로 빌릴 수는 없습니다.
                    user.coin-=1
                    user.save()

                    rental_book.status = '대여중'
                    rental_book.save()

                    #등록한 책이 대여 되었을 때, 업로더의 코인 +2 해줍니다.
                    uploader=UserChangeForm(instance = rental_book.uploader).save(commit=False)
                    uploader.coin+=2
                    uploader.save()

                    messages.success(request, '대여가 성공했습니다!')

                    form=BorrowedBookForm().save(commit=False) #여기부터는 내가 빌린 책 기능을 위해 데이터를 넘겨주는 부분입니다.
                    form.borrower=request.user #로그인 된 유저를 빌린이에 추가합니다
                    form.borrow_book=rental_book#책을 외래키로 저장합니다
                    BorrowedBook=form.save()   
                else:
                      messages.success(request, '자신이 등록한 책은 대여하실 수 없습니다!')     
        else:
            messages.success(request, '코인이 부족합니다!')
        return redirect('book_list')

def myborrowed_book(request):
    me = request.user
    books = BorrowedBook.objects.all().filter(borrower=me).order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'myborrowed_book.html', {'books': books, 'posts':posts})

