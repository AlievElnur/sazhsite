# Generated by Django 4.1.6 on 2023-02-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sazhenci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('message', models.TextField(max_length=2550)),
            ],
        ),
    ]
