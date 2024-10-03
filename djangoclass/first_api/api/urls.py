from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.get_post_users),
    path("users/<int:pk>/", views.get_put_delete_patch_user),
]