from django.views.generic import TemplateView
from book.models import MajorBook

class RentalEditView(TemplateView):
    """
    rental_edit 렌더링 뷰입니다.
    """
    template_name = 'rental/rental_edit.html'

    def get(self, request, id):
        edit_book = MajorBook.objects.get(pk=id)
        context={'book': edit_book}
        return self.render_to_response(context)