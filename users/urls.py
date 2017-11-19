from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^login/$',
        views.UserLoginView.as_view(),
        name='login'
    ),
    url(
        r'^contestants/$',
        views.ContestantsListView.as_view(),
        name='contestant_list'
    ),
    url(
        r'^contestants/(?P<user_id>\d+)/$',
        views.ContestantsDetailView.as_view(),
        name='contestant_detail'
    ),
]
