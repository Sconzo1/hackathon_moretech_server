from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from authentication.managers import AdminManager


class Admin(AbstractBaseUser):
    email = models.EmailField('Почта', unique=True, max_length=100)
    password = models.CharField('Пароль', max_length=300)
    surname = models.CharField('Фамилия', max_length=150)
    name = models.CharField('Имя', max_length=150)
    is_staff = models.BooleanField('Сотрудник?', editable=False, default=True)
    last_login = models.DateTimeField('Время последнего входа', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AdminManager()

    class Meta:
        db_table = 'admins'
        ordering = ['email']
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'

    def __str__(self):
        return f"{self.surname}, {self.name}"

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
