from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router1 = routers.SimpleRouter()
router1.register(
    r'posts',
    PostViewSet,
    basename='posts'
)
router1.register(
    r'groups',
    GroupViewSet,
    basename='groups'
)
router1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router1.register(
    r'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include(router1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
