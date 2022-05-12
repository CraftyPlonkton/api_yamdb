from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet, GenereViewSet, TitleViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r"categories", CategoryViewSet, basename="categories")
router_v1.register(r"genres", GenereViewSet, basename="genres")
router_v1.register(r"titles", TitleViewSet, basename="titles")


urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
