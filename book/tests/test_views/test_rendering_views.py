from django.test import RequestFactory, TestCase
from ...views.template_views import book_list_template_view
from ...views.template_views import categorys_templates_view
from ...views.template_views import mainpage_templates_view
from ...views.template_views import mybook_template_view
from ...views.template_views import myborrowed_book_template_view
from ...views.template_views import mypage
from ...views.template_views import rental_new_template_view

from mixer.backend.django import mixer

class TemplateViewsTest(TestCase):
    """
    Book 패키지의 테스트 클래스입니다.
    """
    def test_book_list_teplate_view(self):
        """
        book_list_teplate_view의 테스트 메서드 입니다.
        """
        request = RequestFactory().get('book/book_list')
        view = book_list_template_view.BookListView()
        view.setup(request)

        context = view.get(request).status_code
        self.assertEqual(context, 200)

    def test_category_teplate_view(self):
        """
        category_teplate_view의 테스트 메서드 입니다.
        """
        request = RequestFactory().get('book/category')
        view=categorys_templates_view.category(request)

        context = view.status_code
        self.assertEqual(context, 200)

    def test_mainpage_teplate_view(self):
        """
        mainpage_teplate_view의 테스트 메서드 입니다.
        """
        request = RequestFactory().get('book')
        view = mainpage_templates_view.MainPageView()
        view.setup(request)

        context = view.get(request).status_code
        self.assertEqual(context, 200)

    def test_mybook_teplate_view(self):
        """
        mybook_teplate_view의 테스트 메서드 입니다.
        """
        request = RequestFactory().get('book/mybook')
        request.user = mixer.blend('account.User')
        view = mybook_template_view.MyBookView()
        view.setup(request)

        context = view.get(request).status_code
        self.assertEqual(context, 200)

    def test_myborrowedbook_teplate_view(self):
        """
        myborrowedbook_teplate_view의 테스트 메서드 입니다.
        """
        request = RequestFactory().get('book/myborrowed_book')
        request.user = mixer.blend('account.User')
        view = myborrowed_book_template_view.MyBorrowedBookView()
        view.setup(request)

        context = view.get(request).status_code
        self.assertEqual(context, 200)

    def test_mypage_teplate_view(self):
        """
        mypage_teplate_view의 테스트 메서드 입니다.
        """
        request = RequestFactory().get('book/mypage')
        request.user = mixer.blend('account.User')
        view = mypage.mypage(request)

        context = view.status_code
        self.assertEqual(context, 200)

    # def test_rental_edit_teplate_view(self):
    #     """
    #     rental_edit_teplate_view의 테스트 메서드 입니다.
    #     """
    #     request = RequestFactory().get('book/rental_edit/<int:pk>')
    #     view =
    #     view.setup(request)
    #
    #     context = view.get(request).status_code
    #     self.assertEqual(context, 200)

    def test_rental_new_teplate_view(self):
        """
        rental_new_teplate_view의 테스트 메서드 입니다.
        """
        request = RequestFactory().get('book/rental_new')
        view = rental_new_template_view.RentalNewView()
        view.setup(request)

        context = view.get(request).status_code
        self.assertEqual(context, 200)

if __name__ == '__main__':
    TemplateViewsTest()