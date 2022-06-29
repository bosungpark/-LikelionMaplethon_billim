# import json
# from ..views.register_books_view import Crud
# from django.test import Client
# from account.models.user_model import User
# from ..models.majorbook_model import MajorBook
# from django.http.request import HttpRequest

# from django.test import TestCase



# class MajorBookTests(TestCase):
#     """
#     전공책 관련 테스트입니다.
#     """

#     # def setUp(self):
#     #     uploader=User.objects.create(email=".", address=".")
#     #     MajorBook.objects.create(title='test', publisher='more testing', author="user", uploader=uploader)

#     def test_creation(self):
#         """
#         전공책 생성 테스트입니다.
#         """
#         c = Client()


#         response = c.post('/book//rental_new', {'title': 'john',
#                                                 'author': 'smith',
#                                                 'publisher': 'smith',
#                                                 'pub_date': '2021-11-11',
#                                                 'category': '기타',
#                                                 'info_text':"." })
#         # print(response.status_code)
#         Crud.post(self, request=response,pk=0)
#         book = MajorBook.objects.get(title='john')
#         print(book.author, "!!!!!!!!!!!!!")
#         self.assertEquals(book.author, 'smith')



# if __name__ == '__main__':
#     MajorBookTests() 