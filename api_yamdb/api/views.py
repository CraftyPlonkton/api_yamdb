from rest_framework import viewsets, filters, mixins, generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.pagination import LimitOffsetPagination

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, tokens
from django.core.mail import send_mail

from reviews.models import Review, Title, Genre, Category
from api.serializers import (
    CommentSerializer,
    ReviewSerializer,
    TitleSerializer,
    GenreSerializer,
    CategorySerializer,
    UserSignUpSerializer
)

User = get_user_model()


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.review.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id, title=title_id)
        serializer.save(author=self.request.user, review=review)

        
# GETlist, POST, DELETE
class CategoryViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser]
    pagination_class = LimitOffsetPagination
    search_fields = ('name',)


# GETlist, POST, DELETE
class GenereViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser]
    pagination_class = LimitOffsetPagination
    search_fields = ('name',)


# GETlist, GET, POST, PATCH, DELETE
class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser]
    pagination_class = LimitOffsetPagination
    search_fields = ('name',)


class UserSignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    permission_classes = (AllowAny,)
