from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import (
    UserListAPIView,
    UserCreateAPIView,
    UserUpdateAPIView,
    UserRetrieveAPIView,
    UserDestroyAPIView,
)

app_name = UsersConfig.name
router = DefaultRouter()

urlpatterns = [
    # User
    path("user/", UserListAPIView.as_view(), name="list_user"),
    path("user/create/", UserCreateAPIView.as_view(), name="create_user"),
    path("user/update/<int:pk>/", UserUpdateAPIView.as_view(), name="update_user"),
    path("user/<int:pk>/", UserRetrieveAPIView.as_view(), name="one_user"),
    path("user/delete/<int:pk>/", UserDestroyAPIView.as_view(), name="delete_user"),

    # Permission
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
