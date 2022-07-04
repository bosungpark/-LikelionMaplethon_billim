from django.contrib import admin
from .models import MajorBook, BorrowedBook

admin.site.register(MajorBook)
admin.site.register(BorrowedBook)