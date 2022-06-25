from django.urls import path
from .mail_view import *

urlpatterns = [
     path('', mail, name="mail"),
]