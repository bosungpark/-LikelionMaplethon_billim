from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from ..models import MajorBook, BorrowedBook
from ..forms import BookForm, BorrowedBookForm
from django.contrib import messages

def mybook(request):
    """
    내가 등록한 책 목록
    """
    me = request.user
    books = MajorBook.objects.all().filter(uploader=me).order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'mybook.html', {'books': books, 'posts':posts})

def detail(request, pk):
    """
    책 상세 페이지
    """
    book = MajorBook.objects.get(pk=pk)
    return render(request, 'rental_detail.html', {'book':book})

def new(request):
    """
    책 등록하기 함수
    """
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.upload_date = timezone.now()
            post.uploader = request.user
            if not post.img:#만약 등록한 이미지가 없다면 크롤링하여 보여줍니다.
                img_url=crawler(post.title)
                post.crawling_img_url = img_url
            post.save()
        else:
            messages.error(request, '형식에 맞게 다시 등록해주세요')
        return redirect('book_list')
    else:  #글을 쓰기위해 들어갔을 때
        form = BookForm()
        return render(request,'rental_new.html', {'form':form})

def edit(request, pk):
    """
    수정 함수
    """
    edit_book = MajorBook.objects.get(pk=pk)
    return render(request, 'rental_edit.html', {'book':edit_book})

def update(request, pk):
    """
    수정함수
    """
    update_book = MajorBook.objects.get(pk=pk)
    update_book.title = request.POST['title']
    update_book.author = request.POST['author']
    update_book.publisher = request.POST['publisher']
    update_book.pub_date = request.POST['pub_date']
    update_book.upload_date = timezone.now()
    update_book.info_text = request.POST['info_text']
    update_book.status = request.POST['status']
    update_book.save()
    return redirect('detail', update_book.pk)

def delete(request, pk):
    """
    삭제함수
    """
    delete_book = MajorBook.objects.get(pk=pk)
    delete_book.delete()
    return redirect('book_list')