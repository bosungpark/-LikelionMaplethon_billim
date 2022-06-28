from django.urls import path
from .views import *

urlpatterns = [
    path('notice/', NoticeView.as_view(), name="notice"),
    path('guide/', GuideView.as_view(), name="guide"),
    path('producer/', ProducerView.as_view(), name="producer"),
]
