# YaMDb API

### Описание проекта:

Проект YaMDb собирает отзывы пользователей на произведения, позволяет ставить произведениям оценку и комментировать чужие отзывы.

Произведения делятся на категории, и на жанры. Список произведений, категорий и жанров может быть расширен администратором.

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Доступ к БД проекта осуществляется через Api.

Полный список запросов и эндпоинтов описан в документации ReDoc, доступна после запуска проекта по адресу:
```
http://127.0.0.1:8000/redoc/
```

### Как запустить проект на тестовом сервере:
Клонировать репозиторий, перейти в директорию с проектом.

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/source/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 api_yamdb/manage.py migrate
```

Запустить проект:

```
python3 api_yamdb/manage.py runserver
```

### Авторизация пользователей:
Для получения доступа необходимо создать пользователя отправив POST запрос на эндпоинт ```/api/v1/auth/signup/``` username и email

Запрос:
```
{
"email": "string",
"username": "string"
}
```
После этого на email придет код подтверждения, который вместе с username необходимо отправить POST запросом на эндпоинт```/api/v1/auth/token/```

Запрос:
```
{
"username": "string",
"confirmation_code": "string"
}
```
Ответ:
```
{
"access": "string"
}
```
Полученный токен используется для авторизации

Для просмотра и изменения своих данных используйте эндпоинт ```/api/v1/users/me/```

### Примеры запросов к API:

Получение списка всех категорий:

```
http://127.0.0.1:8000/api/v1/categories/
```
Получение списка всех жанров:

```
http://127.0.0.1:8000/api/v1/genres/
```

Получение списка всех произведений:

```
http://127.0.0.1:8000/api/v1/titles/
```
