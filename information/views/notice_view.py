from django.views.generic import TemplateView

class NoticeView(TemplateView):
    template_name = 'notice.html'

    def get(self, request, *args, **kwargs):
        context={}
        return self.render_to_response(context)