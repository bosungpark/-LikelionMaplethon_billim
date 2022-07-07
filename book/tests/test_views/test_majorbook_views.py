from django.test import Client
from django.test import TestCase

from book.forms import BookForm
from book.models.majorbook_model import MajorBook

class MajorBookTests(TestCase):
    """
    전공책 관련 테스트입니다.
    """

    def test_creation_rendering(self):
        """
        전공책 생성페이지 렌더링 테스트입니다.
        """
        c = Client()
        response = c.post('/book/rental_new', {'title': 'john',
                                                'author': 'smith',
                                                'publisher': 'smith',
                                                'pub_date': '2021-11-11',
                                                'category': '기타',
                                                'info_text':"." })
        self.assertEqual(response.status_code,301)

    def test_creation(self):
        """
        전공책 생성 테스트입니다.
        """
        c = Client()
        response = c.post('/book/crud', {'title': 'john',
                                                'author': 'smith',
                                                'publisher': 'smith',
                                                'pub_date': '2021-11-11',
                                                'category': '기타',
                                                'info_text':"." })
        self.assertEqual(response.status_code,302)

    # def test_edit_rendering(self):
    #     """
    #     전공책 수정 페이지 렌더링 테스트입니다.
    #     """
    #     c = Client()
    #     response = c.put('/book/rental_edit/<int:pk>')
    #     self.assertEqual(response.status_code,301)

    # def test_edit(self):
    #     """
    #     전공책 수정 테스트입니다.
    #     """
    #     m=MajorBook.objects.get(pk=1)
    #     if m:
    #         c = Client()
    #         response = c.put('/book/crud/1', {'title': 'john',
    #                                                 'author': 'smith',
    #                                                 'publisher': 'smith',
    #                                                 'pub_date': '2021-11-11',
    #                                                 'category': '기타',
    #                                                 'info_text':"!" })
    #     else:
    #         pass
    #     # print(response.status_code)
    #     self.assertEqual(response.status_code,301)

if __name__ == '__main__':
    MajorBookTests()