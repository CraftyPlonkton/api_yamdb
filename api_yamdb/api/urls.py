from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ReviewViewSet,
    CommentViewSet,
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    UserSignUpView,
    TokenCreateView,
    UserViewSet,
    UserMeView
)


v1_router = DefaultRouter()
v1_router.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                   r'/comments', CommentViewSet, basename='comments')
v1_router.register(r"categories", CategoryViewSet, basename="categories")
v1_router.register(r"genres", GenreViewSet, basename="genres")
v1_router.register(r"titles", TitleViewSet, basename="titles")
v1_router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/signup/', UserSignUpView.as_view()),
    path('v1/auth/token/', TokenCreateView.as_view()),
    path(r'v1/users/me/', UserMeView.as_view()),
    path('v1/', include(v1_router.urls)),
]
