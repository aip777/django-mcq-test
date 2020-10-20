from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home),
    path('question', question),
    path('qus', create_question),
    path('create', StudentCreateView.as_view(),name='create'),
    # path('questionlistans', QuestionViewList.as_view(),name='questionviewlist'),
    path('questionlist', QuestionView.as_view(),name='questionlist'),
    path('update/<int:pk>', StudentUpdateView.as_view(),name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('search/', ProfileList.as_view(), name='search'),

]