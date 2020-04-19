from django.urls import path
from . import views
from .feeds import LatestPostsFeed

# app-name = 'polls'
urlpatterns = [
    # indexs
    # path('', views.index, name="index"),
    path("", views.post_list, name="post_list"),
    # path("", views.PostListView.as_view(), name="post_list"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_list_by_tag"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path('feed/', LatestPostsFeed(), name='post-feed'),
    path('search/', views.post_search, name='post_search'),
]
