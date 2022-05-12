from rest_framework import filters
from rest_framework import viewsets
from .models import Titles, Generes, Categories
from .serializers import (
    TitleSerializer,
    GenereSerializer,
    CategorySerializer,
)
from rest_framework import filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import LimitOffsetPagination


# GETlist, POST, DELETE
class CategoryViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    mixins.DeleteModelMixin, viewsets.GenericViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter)
    permission_classes = [IsAdminUser]
    pagination_class = LimitOffsetPagination
    search_fields = ('name',)

# GETlist, POST, DELETE
class GenereViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    mixins.DeleteModelMixin, viewsets.GenericViewSet):
    queryset =Generes.objects.all()
    serializer_class = GenereSerializer
    filter_backends = (filters.SearchFilter)
    permission_classes = [IsAdminUser]
    pagination_class = LimitOffsetPagination
    search_fields = ('name',)

# GETlist, GET, POST, PATCH, DELETE
class TitleViewSet(viewsets.ModelViewSet):
    queryset =Titles.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (filters.SearchFilter)
    permission_classes = [IsAdminUser]
    pagination_class = LimitOffsetPagination
    search_fields = ('name',)
