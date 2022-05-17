from django.contrib import admin

from .models import Title, Review, Comment, Category, Genre, GanreTitle


admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(GanreTitle)
