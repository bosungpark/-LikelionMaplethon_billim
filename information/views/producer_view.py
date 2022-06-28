from django.views.generic import TemplateView

class ProducerView(TemplateView):
    template_name = 'producer.html'

    def get(self, request, *args, **kwargs):
        context={}
        return self.render_to_response(context)