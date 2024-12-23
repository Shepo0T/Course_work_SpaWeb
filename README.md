# Course_work_SpaWeb Upit Aleksandr

Трекер полезных привычек
Бэкенд-часть SPA веб-приложения "Трекер полезных привычек".

> Выполнил Упит Александр


Для начала работы произведите:
1. Клонирование данного репозитория
2. Настройте виртуальное окружение `Poetry`, установив все пакеты для работы с проектом
3. Произведите настройку проекта в файле .env.sample, добавив указанные параметры
4. Создайте список привычек
5. Использовав команду `python3 manage.py csu`  вы создадите учетную запись администратора ( данные которой можно посмотреть в приложении users )



















![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)



Для запуска проекта в Docker необходимо:

1) Клонируете данный проект к себе на рабочую станцию
2) Настройте переменные окружения по шаблону ".env.sample"
3) Произведите запуск сборки контейнеров с помощью команду `docker compose up -d --build`
4) После удачной сборки контейнера используйте данную команду загрузки фикстур`docker compose exec spa_app python manage.py loaddata /spa_app/users.json && docker compose exec spa_app python manage.py loaddata /spa_app/habits.json`
%% Порядок команд не изменять во избежание сбоя!!! %%

Дальше открываете необходимые ссылки проекта
