from http.client import responses

import requests
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.reverse import reverse
from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def send_telegram_message(chat_id, message):

    params = {
        'text': message,
        'chat_id': chat_id,
    }
    response = requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)

    if response.status_code == status.HTTP_400_BAD_REQUEST:
        raise APIException(f'Cначала начните диалог с telegram-ботом! Получить ссылку на бота вы можете '
                           f'по URL-адресу: {reverse("habits:tg_bot_link")}')

