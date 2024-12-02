from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habits
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@project.upit")
        self.user.set_password("admin")
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habits.objects.create(
            owner=self.user,
            act="Сделать зарядку",
            pleasant_habit=True,
            when_to_perform="18:26:17",
            location="Дом",
            time_to_complete="00:01:30"
        )

    def test_create_habit(self):
        """Test creating a habit."""
        url = reverse("habits:habits_create")
        data = {
            "owner": self.user.pk,
            "act": "Убрать лишние вещи",
            "pleasant_habit": True,
            "when_to_perform": "18:26:17",
            "location": "Дом",
            "time_to_complete": "00:02:00"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.count(), 2)
        self.assertTrue(Habits.objects.all().exists())

    def test_habit_list(self):
        """Test that habit list works"""
        url = reverse("habits:habits_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "act": "Сделать зарядку",
                    "associated_habit": None,
                    "id": self.habit.pk,
                    "is_public": True,
                    "location": "Дом",
                    "owner": self.user.pk,
                    "periodicity": 1,
                    "pleasant_habit": True,
                    "reward": None,
                    "time_to_complete": "00:01:30",
                    "when_to_perform": "18:26:17",



                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_retrieve(self):
        """Test that retrieve returns correct data"""
        url = reverse("habits:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["location"], self.habit.location)

    def test_habit_update(self):
        """Test that works update habits"""
        url = reverse("habits:habits_update", args=(self.habit.pk,))
        data = {
            "act": "Побегать на дорожке",
        }
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["act"], "Побегать на дорожке")

    def test_habit_delete(self):
        url = reverse("habits:habits_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.count(), 0)
