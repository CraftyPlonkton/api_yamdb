from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведения',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    scope = models.IntegerField(
        verbose_name='Рейтинг',

    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['pub_date']


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['pub_date']

        
class Categories(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(
        max_length=50, unique=True,
    )

    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(
        max_length=50, unique=True,
    )

    def __str__(self):
        return self.name

class Titles(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    description = models.TextField()
    genre = models.ForeignKey(
        Genres, on_delete=models.CASCADE, related_name='titles')
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name='titles')

    def __str__(self):
        return self.name
