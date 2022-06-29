from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from ..models import MajorBook
from ..forms import BookForm
from django.contrib import messages
from django.views import View
from .utils import crawler


class Crud(View):
    def get(self,request, pk):
        """
        책 상세 페이지
        """
        book = MajorBook.objects.get(pk=pk)
        return render(request, 'rental_detail.html', {'book':book})

    def post(self,request, pk):
        """
        책 등록하기 함수
        """
        # print(request)
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.upload_date = timezone.now()
            post.uploader = request.user
            # 만약 등록한 이미지가 없다면 크롤링하여 보여줍니다.
            if not post.img:
                img_url=crawler(post.title)
                post.crawling_img_url = img_url
            post.save()
        else:
            messages.error(request, '형식에 맞게 다시 등록해주세요')
        return redirect('book_list')

    def put(self,request, pk):
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
        return redirect('crud', update_book.pk)

    def delete(self, pk):
        """
        삭제함수
        """
        delete_book = MajorBook.objects.get(pk=pk)
        delete_book.delete()
        return redirect('book_list')

def mybook(request):
    """
    내가 등록한 책 목록 랜더링 함수입니다.
    """
    me = request.user
    books = MajorBook.objects.all().filter(uploader=me).order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'mybook.html', {'books': books, 'posts':posts})

def rental_new(request):
    """
    rental_new 렌더링 함수입니다.
    """
    form = BookForm()
    return render(request, 'rental_new.html', {'form': form})

def rental_edit(request,pk):
    """
    rental_edit 렌더링 함수입니다.
    """
    edit_book = MajorBook.objects.get(pk=pk)
    return render(request, 'rental_edit.html', {'book': edit_book})