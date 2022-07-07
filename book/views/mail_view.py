from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse

class MailView(TemplateView):
    """
    mybook 렌더링 뷰입니다.
    """
    template_name = 'mail/mail.html'

    def get(self, request):
        context={}
        return self.render_to_response(context)

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        Username: {} 
        Message: {}
        From: {}
        '''.format(data['name'], data['message'], data['email'])
        send_mail(data['subject'], message, email, ['yolllllim@gmail.com'])
        return HttpResponse('Thank you for sending the mail.')

