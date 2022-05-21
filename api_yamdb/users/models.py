from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Пользователь'),
        ('moderator', 'Модератор'),
        ('admin', 'Администратор')
    )
    password = models.CharField('password', max_length=128, default=False)
    bio = models.TextField('Биография', blank=True)
    email = models.EmailField('email адрес', max_length=254, unique=True)
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=256,
        blank=True
    )
    role = models.CharField(
        'Права доступа',
        max_length=30,
        choices=ROLE_CHOICES,
        default='user'
    )

    class Meta:
        ordering = ['-date_joined']
        constraints = [
            models.CheckConstraint(
                check=~models.Q(username='me'),
                name='username_not_me')
        ]

    def is_admin(self):
        if self.role in ['admin'] or self.is_superuser:
            return True

    def is_moderator(self):
        if self.role in ['moderator']:
            return True

    def __str__(self):
        return self.username
