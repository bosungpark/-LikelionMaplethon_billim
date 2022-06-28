from django.views.generic import TemplateView

class GuideView(TemplateView):
    template_name = 'guide.html'

    def get(self,request):
        context={}
        return self.render_to_response(context)