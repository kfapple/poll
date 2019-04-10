from django.urls import path
from .views import *

urlpatterns = [
    #path('poll/', poll_list),
    path('poll/', polllist.as_view()),
    path('poll/<int:pk>/',PollDetail.as_view())
]
