from django.urls import path
from .views import *

urlpatterns = [
    path('poll/', poll_list),
    path('poll1/', polllist.as_view()),
]
