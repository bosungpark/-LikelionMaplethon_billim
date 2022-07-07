from django.views.generic import TemplateView
from django.core.paginator import Paginator
from book.models import MajorBook

class MyBookView(TemplateView):
    """
    mybook 렌더링 뷰입니다.
    """
    template_name = 'mybook/mybook.html'

    def get(self, request):
        me = request.user
        books = MajorBook.objects.all().filter(uploader=me).order_by('-id')
        paginator = Paginator(books, 8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context={'books': books, 'posts':posts}
        return self.render_to_response(context)