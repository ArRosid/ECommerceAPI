from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("products", views.ProductViewSet)

urlpatterns = [
    path("products/featured/", views.ProductFeaturedList.as_view(), name="product-featured"),
    path("", include(router.urls)),
]