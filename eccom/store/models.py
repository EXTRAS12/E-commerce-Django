from tabnanny import verbose
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    user = models.ForeignKey(User, related_name='products',
                             on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Слаг')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price