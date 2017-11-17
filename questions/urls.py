from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^single/(?P<pk>\d+)/$',
        views.SingleQuestionView.as_view(),
        name='single_detail'
    ),
    url(
        r'^multiple/(?P<pk>\d+)/$',
        views.MutipleQuestionView.as_view(),
        name='multiple_detail'
    ),
]
