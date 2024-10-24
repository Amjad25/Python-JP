from rest_framework.routers import DefaultRouter
from .views import *

from django.urls import path

router = DefaultRouter()
router.register('category',CategoryViewSet)
router.register('supplier',SupplierviewSet)
router.register('product',ProductviewSet)


urlpatterns = [
    path('category/<int:id>' ,SupplierRetrieveUpdateDestroyAPIView.as_view()),
    path('suppliers' ,SupplierListCreateAPIView.as_view())
]+router.urls