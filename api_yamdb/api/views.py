from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.db.models import Avg

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters, mixins, views, status
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from reviews.models import Review, Title, Genre, Category
from .permissions import (
    IsAdminOrSuperuserOnly,
    IsAdminOrReadOnly,
    IsAuthenticatedOrReadOnly
)
from .serializers import (
    CommentSerializer,
    ReviewSerializer,
    TitleSerializer,
    GenreSerializer,
    CategorySerializer,
    UserSignUpSerializer,
    TokenCreateSerializer,
    UserSerializer,
    RatingSerializer
)
from .filters import TitleFilter

User = get_user_model()


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id, title__id=title_id)
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id, title__id=title_id)
        serializer.save(author=self.request.user, review=review)


# GETlist, POST, DELETE
class CategoryViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    search_fields = ('name',)


# GETlist, POST, DELETE
class GenreViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                   mixins.DestroyModelMixin, viewsets.GenericViewSet):
    lookup_field = 'slug'
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    search_fields = ('name',)


# GETlist, GET, POST, PATCH, DELETE
class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action in ("retrieve", "list"):
            return RatingSerializer
        return TitleSerializer

    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = TitleFilter

    def get_queryset(self):
        queryset = Title.objects.all().annotate(
            Avg("reviews__score")).order_by("name")
        return queryset


class UserSignUpView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        confirmation_code = get_random_string(length=30)
        serializer.save(confirmation_code=confirmation_code)
        send_mail(
            'Subject',
            f'Your confirmation code {confirmation_code}',
            'from@example.com',
            [serializer.validated_data['email']],
        )
        return Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK
        )


class TokenCreateView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            data={'access': str(serializer.validated_data)},
            status=status.HTTP_200_OK
        )


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated & IsAdminOrSuperuserOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['username']

    @action(
        detail=False, methods=['get', 'patch'],
        permission_classes=(IsAuthenticated,)
    )
    def me(self, request):
        user = self.request.user
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        if request.method == 'PATCH':
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                if serializer.validated_data.get('role'):
                    serializer.validated_data.pop('role')
                serializer.save()
                return Response(serializer.data)
