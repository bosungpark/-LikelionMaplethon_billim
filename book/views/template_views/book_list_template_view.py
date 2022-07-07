from django.views.generic import TemplateView
from django.core.paginator import Paginator
from book.models import MajorBook

class BookListView(TemplateView):
    """
    책 대여하기 렌더링 뷰 입니다.
    """
    template_name = 'rental/rental_main.html'

    def get(self, request):
        books = MajorBook.objects.all().order_by('-id')
        paginator = Paginator(books, 8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context={'books': books, 'posts':posts}
        return self.render_to_response(context)