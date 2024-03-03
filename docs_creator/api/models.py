from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class File(models.Model):
    """Модель файла"""
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Укажите название файла')
    data = models.TextField(
        verbose_name='Данные документа',
        help_text='Заполните текстовое наполнение файла')

    def __str__(self):
        return self.name
