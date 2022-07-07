from django.views.generic import TemplateView
from django.core.paginator import Paginator
from ...models import MajorBook, BorrowedBook

class MyBorrowedBookView(TemplateView):
    """
    내가 대여한 책 렌더링 뷰 입니다.
    """
    template_name = 'mybook/myborrowed_book.html'

    def get(self, request):
        me = request.user
        books = BorrowedBook.objects.all().filter(borrower=me).order_by('-id')
        paginator = Paginator(books, 8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context={'books': books, 'posts':posts}
        return self.render_to_response(context)