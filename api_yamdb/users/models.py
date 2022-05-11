from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Пользователь'),
        ('moderator', 'Модератор'),
        ('admin', 'Администратор')
    )
    bio = models.TextField('Биография', blank=True)
    email = models.EmailField('email адрес', max_length=254, unique=True)
    confirmation_code = models.TextField(
        'Код подтверждения',
        blank=True
    )
    role = models.CharField(
        'Првава доступа',
        max_length=30,
        choices=ROLE_CHOICES,
        default='user'
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~models.Q(username='me'),
                name='username_not_me')
        ]

    def __str__(self):
        return self.username
