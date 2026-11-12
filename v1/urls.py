from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('contact/', ContactAPI.as_view())
]

urlpatterns += router.urls

