from django.shortcuts import render, redirect
from django.utils import timezone
from ..models import MajorBook
from ..forms import BookForm
from django.contrib import messages
from django.views import View
from .utils import crawler


class Crud(View):
    http_method_names = ['get', 'post', 'put', 'delete']

    def dispatch(self, *args, **kwargs):
        """
        html form은 put과 delete를 지원하지 않으므로, 직접 분기를 처리해 작업해주었습니다.
        """
        if self.request.POST:
            method = self.request.POST.get('_method', '').lower()
            if method == 'put':
                return self.put(*args, **kwargs)
            elif method == 'delete':
                return self.delete(*args, **kwargs)
            else:
                return self.post(*args, **kwargs)
        else:
            return self.get(*args, **kwargs)

    def get(self,request, pk):
        """
        책 상세 페이지
        """
        book = MajorBook.objects.get(pk=pk)
        return render(request, 'rental/rental_detail.html', {'book':book})

    def post(self,request):
        """
        책 등록하기 함수
        """
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
        return redirect('book_list')

    def delete(self, pk):
        """
        삭제함수
        """
        delete_book = MajorBook.objects.get(pk=pk)
        delete_book.delete()
        return redirect('book_list')