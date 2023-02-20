from django.db import models
from django.urls import reverse


class Rasteniya(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название сорта')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Текст Сорта')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    lef = models.ForeignKey('Left', on_delete=models.PROTECT, verbose_name='Каталог')
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
    
    class Meta:
        verbose_name = 'Сорта Саженцев'
        verbose_name_plural = 'Сорта Саженцев'
        ordering = ['lef', 'title']
    

class Left(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Каталог сортов')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("left", kwargs={"lef_slug": self.slug})

    class Meta:
        verbose_name = 'Каталог сортов'
        verbose_name_plural = 'Каталог сортов'
        ordering = ['id']


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=2550)

    def __str__(self):
        return self.email