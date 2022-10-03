from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router1 = routers.SimpleRouter()
router1.register(r'posts', PostViewSet)
router1.register(r'groups', GroupViewSet)
router1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router1.register(r'follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(router1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
