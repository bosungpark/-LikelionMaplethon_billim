from django import forms
from ..models.majorbook_model import MajorBook

class BookForm(forms.ModelForm):
    class Meta:
        model = MajorBook
        fields = ['title', 'author', 'publisher', 'pub_date', 'category', 'img', 'info_text', 'status']