from ..models.majorbook_model import MajorBook
from account.models.user_model import User

from django.test import TestCase


class MajorBookTests(TestCase):
    """
    전공책 관련 테스트입니다.
    """

    def setUp(self):
        uploader = User.objects.create(email=".", address=".")
        MajorBook.objects.create(title='test', publisher='more testing', author="user", uploader=uploader)

    def test_creation(self):
        """
        전공책 생성 테스트입니다.
        """
        book = MajorBook.objects.get(title='test')
        self.assertEquals(book.author, 'user')


if __name__ == '__main__':
    MajorBookTests()