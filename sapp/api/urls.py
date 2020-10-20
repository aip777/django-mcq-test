from django.conf.urls import url


from .views import (
    StudentAPIView,
    StudentAPIDetailView,
    StatusAPIView,
    StatusAPIDetailView
)
urlpatterns = [
    # url(r'^$', StudentAPIView.as_view()),
    # url(r'^(?P<id>\d+)/$', StudentAPIDetailView.as_view()),
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()),
]