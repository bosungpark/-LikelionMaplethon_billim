from django.db import models
from django.conf import settings
from .majorbook_model import MajorBook


class BorrowedBook(models.Model):
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 빌리는 사람
    borrow_book = models.ForeignKey(MajorBook, on_delete=models.CASCADE)  # 책의 pk값
    borrowed_date = models.DateTimeField(auto_now=True, null=True)  # 빌린 날짜

    def __str__(self):
        return self.borrow_book.title