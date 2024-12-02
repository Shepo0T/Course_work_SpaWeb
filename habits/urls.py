from django.urls import path

from habits.apps import HabitsConfig

from habits.views import (
    HabitsListAPIView,
    HabitsCreateAPIView,
    HabitsUpdateAPIView,
    HabitsRetrieveAPIView,
    HabitsDestroyAPIView,
    HabitsPublicListAPIView
)

app_name = HabitsConfig.name

urlpatterns = [
    path(
        'habits/',
        HabitsListAPIView.as_view(),
        name='habits_list'
    ),
    path(
        'habit/<int:pk>/',
        HabitsRetrieveAPIView.as_view(),
        name='habits_retrieve'
    ),
    path(
        'habit/create/',
        HabitsCreateAPIView.as_view(),
        name='habits_create'
    ),
    path(
        'habit/<int:pk>/update/',
        HabitsUpdateAPIView.as_view(),
        name='habits_update'
    ),
    path(
        'habit/<int:pk>/delete/',
        HabitsDestroyAPIView.as_view(),
        name='habits_delete'
    ),
    path(
        'public/',
        HabitsPublicListAPIView.as_view(),
        name='public_list'
    )
]
