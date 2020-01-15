from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register("category", views.CategoryViewSet)
router.register("product", views.ProductViewSet)

urlpatterns = [
    path("", include(router.urls))
]

