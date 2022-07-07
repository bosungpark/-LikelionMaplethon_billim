from django.views.generic import TemplateView
from django.core.paginator import Paginator
from book.models import MajorBook
from solution.models import Solution

class MainPageView(TemplateView):
    """
    메인 페이지 함수 렌더링 뷰 입니다.
    """
    template_name = 'mainpage.html'

    def get(self, request):
        b = MajorBook.objects.all().order_by('-id')
        book_paginator = Paginator(b, 4)
        book = request.GET.get('page')
        books = book_paginator.get_page(book)

        s = Solution.objects.all().order_by('-id')
        solution_paginator = Paginator(s, 4)
        solutions = solution_paginator.get_page(book)

        contents = Solution.objects.all().order_by('-id')

        context={'books' : books, 'solutions' : solutions,'contents' : contents}
        return self.render_to_response(context)