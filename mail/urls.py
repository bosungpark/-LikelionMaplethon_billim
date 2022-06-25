from django.urls import path
from .views.mail_view import *

urlpatterns = [
     path('', mail, name="mail"),
]