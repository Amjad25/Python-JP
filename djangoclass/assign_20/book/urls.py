from django.urls import path
from .views import *

urlpatterns = [
    path('', books),
    path('<int:id>', book),
    path('authors/', authors),
    path('author/<int:id>', author),
    path('genres/', genres),
    path('genre/<int:id>', genre),
]
