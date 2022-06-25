from django import forms
from ..models.borrowedbook_model import BorrowedBook

class BorrowedBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['borrower','borrow_book']