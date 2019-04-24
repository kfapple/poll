from django.urls import path
from .views import *

urlpatterns = [
    #path('poll/', poll_list),
    path('poll/', polllist.as_view()),
    path('poll/<int:pk>/',PollDetail.as_view()),
    path('vote/<int:pk>/',PollVote.as_view()),
    path('vote/create/',PollCreate.as_view()),
    path('poll/<int:pk>/update/',PollUpdate.as_view()),
    path('poll/<int:pk>/delete/',PollDelete.as_view()),
    path('option/create/<int:pid>',OptionCreate.as_view()),
]
