# Generated by Django 3.2.7 on 2021-10-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Почта')),
                ('password', models.CharField(max_length=300, verbose_name='Пароль')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('is_staff', models.BooleanField(default=True, editable=False, verbose_name='Сотрудник?')),
                ('last_login', models.DateTimeField(null=True, verbose_name='Время последнего входа')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'admins',
                'ordering': ['email'],
            },
        ),
    ]