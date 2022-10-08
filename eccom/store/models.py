from django.contrib.auth.models import User
from django.db import models
from django.core.files import File

from io import BytesIO
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    DRAFT = 'Черновик'
    WAITING_APPROVAL = 'Ожидает подтверждения'
    ACTIVE = 'Активный'
    DELETED = 'Удалён'

    STATUS_CHOICES = (
        (DRAFT, 'Черновик'),
        (WAITING_APPROVAL, 'Ожидает подтверждения'),
        (ACTIVE, 'Активный'),
        (DELETED, 'Удалён'),
    )

    user = models.ForeignKey(
        User, related_name='products', on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Слаг')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/product_images', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/product_images/thumbnail', blank=True, null=True)
    status = models.CharField(
        max_length=50, verbose_name='Статус', choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        name = image.name.replace('uploads/product_images/', '')
        thumbnail = File(thumb_io, name=name)

        return thumbnail
