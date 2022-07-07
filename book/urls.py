from django.urls import path
from .views.borrow_books_view import *
from .views.utils import *
from .views.mypage import *
from .views.mainpage import *
from .views.categorys import *
from .views.register_books_view import *
from .views.mail_view import *


urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('rental_new/', rental_new, name="rental_new"),
    path('rental_edit/<int:id>', rental_edit, name="rental_edit"),

    path('book_list', book_list, name="book_list"),
    path('crud/<int:pk>', Crud.as_view(), name="crud"),

    path('rental/<str:id>', rental, name="rental"),
    path('mypage/', mypage, name="mypage"),

    path('category', category, name="category"),

    path('mybook/', mybook, name="mybook"),
    path('myborrowed_book/', myborrowed_book, name="myborrowed_book"),
    path('search/', search, name="search"),
    path('placeholder/', placeholder, name="placeholder"),
    path('mail/', mail, name="mail"),
]
