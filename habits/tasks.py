from celery import shared_task
from datetime import datetime
from habits.models import Habits
from habits.services import send_telegram_message
from users.models import User


@shared_task
def send_habit():
    habits = Habits.objects.all()
    users = User.objects.filter(tg_chat_id__isnull=False)

    current_time = datetime.now().strftime("%H:%M:%S")

    for user in users:
        for habit in habits:
            if habit.owner == user:
                habit_start_time = habit.when_to_perform.strftime("%H:%M:%S")

                if habit_start_time == current_time:
                    message = f"Не забудь, что нужно: {habit.act}, время выполнения: {habit.time_to_complete} минуты."

                    if habit.pleasant_habit:
                        message = (f"Не забудь, что нужно: {habit.act},"
                                   f" время выполнения: {habit.time_to_complete} минуты.")
                    if habit.associated_habit:
                        message = (f""
                                   f"Не забудь, что нужно: "
                                   f"{habit.act}, время выполнения: "
                                   f"{habit.time_to_complete} минуты, затем можешь: "
                                   f"{habit.associated_habit}.")
                    if habit.reward:
                        message = (f"Необходимо сделать: {habit.act},"
                                   f" время выполнения: {habit.time_to_complete} минуты, "
                                   f"за это получишь в награду: {habit.reward}.")

                    send_telegram_message(habit.owner.tg_chat_id, message)
                    habit.save()
