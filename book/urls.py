from django.urls import path
from book.views.rental import *
from .views.utils import *
from book.views.template_views.mypage import *
from book.views.template_views.categorys_templates_view import *
from .views.crud_view import *
from .views.mail_view import *
from .views.template_views.mybook_template_view import *
from .views.template_views.rental_edit_template_view import *
from .views.template_views.rental_new_template_view import *
from .views.template_views.book_list_template_view import *
from .views.template_views.myborrowed_book_template_view import *
from .views.template_views.mainpage_templates_view import *


urlpatterns = [
    path('', MainPageView.as_view(), name="mainpage"),
    path('rental_new/', RentalNewView.as_view(), name="rental_new"),
    path('mybook/', MyBookView.as_view(), name="mybook"),
    path('myborrowed_book/', MyBorrowedBookView.as_view(), name="myborrowed_book"),
    path('rental_edit/<int:id>', RentalEditView.as_view(), name="rental_edit"),
    path('book_list', BookListView.as_view(), name="book_list"),
    path('category', category, name="category"),
    path('mypage/', mypage, name="mypage"),

    path('crud', Crud.as_view(), name="crud"),
    path('crud/<int:pk>', Crud.as_view(), name="crud"),
    path('rental/<str:id>', rental, name="rental"),
    path('mail/', MailView.as_view(), name="mail"),
    path('search/', search, name="search"),
    path('placeholder/', placeholder, name="placeholder"),
]
