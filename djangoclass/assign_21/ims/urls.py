from django.urls import path
from .views import products,product,categories, category, suppliers ,supplier

urlpatterns = [
    path('products', products),
    path('product/<int:id>', product),
    path('categories', categories),
    path('category/<int:id>', category),
    path('suppliers', suppliers),
    path('suppliers/<int:id>', supplier),
]