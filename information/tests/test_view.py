import os
from distutils.util import strtobool

os.environ.setdefault("DJANGO_SETTINGS_MODULE","billim.settings")


from django.test import RequestFactory, TestCase
from ..views.guide_view import GuideView
from ..views.notice_view import NoticeView
from ..views.producer_view import ProducerView

class HomePageTest(TestCase):
    """
    information 패키지의 테스트 클래스입니다.
    """
    def test_guide_view(self):
        """
        GuideView의 테스트 메서드 입니다.
        """
        request = RequestFactory().get('/information/guide')
        view = GuideView()
        view.setup(request)

        context = view.get(request).status_code
        self.assertEqual(context, 200)

    def test_notice_view(self):
        """
        NoticeView의 테스트 메서드 입니다.
        """
        request = RequestFactory().get('/information/notice')
        view = NoticeView()
        view.setup(request)

        context = view.get(request).status_code
        self.assertEqual(context, 200)

    def test_producer_view(self):
        """
        NoticeView의 테스트 메서드 입니다.
        """
        request = RequestFactory().get('/information/producer')
        view = ProducerView()
        view.setup(request)

        context = view.get(request).status_code
        self.assertEqual(context, 200)

if __name__ == '__main__':
    HomePageTest()