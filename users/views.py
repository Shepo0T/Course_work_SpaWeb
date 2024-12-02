from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.serializers import UserSerializers

from users.models import User


class UserCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания пользователя"""
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка пользователей"""
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра одного пользователя"""
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для редактирования пользователя"""
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления пользователя"""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
