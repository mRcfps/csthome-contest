from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^login/$',
        views.UserLoginView.as_view(),
        name='login'
    ),
    url(
        r'^scores/$',
        views.ScoreBoardView.as_view(),
        name='scores'
    ),
]
