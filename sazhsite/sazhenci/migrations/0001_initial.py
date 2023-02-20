# Generated by Django 4.1.6 on 2023-02-11 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Left',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Каталог сортов')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Каталог сортов',
                'verbose_name_plural': 'Каталог сортов',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rasteniya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название сорта')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Текст Сорта')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('lef', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sazhenci.left', verbose_name='Каталог')),
            ],
            options={
                'verbose_name': 'Сорта Саженцев',
                'verbose_name_plural': 'Сорта Саженцев',
                'ordering': ['lef', 'title'],
            },
        ),
    ]
