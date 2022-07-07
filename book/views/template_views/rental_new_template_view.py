from django.views.generic import TemplateView
from book.forms import BookForm

class RentalNewView(TemplateView):
    """
    rental_new 렌더링 뷰입니다.
    """
    template_name = 'rental/rental_new.html'

    def get(self, request):
        form = BookForm()
        context={'form': form}
        return self.render_to_response(context)