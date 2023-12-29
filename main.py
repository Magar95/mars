from  django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime


class Device(models.Model):
    """Оборудование"""

    class Meta:
        dv_table = 'devices'
        verbose_name = 'Доступное оборудование'
        verbose_name_plural = 'Доступное оборудование'

    manufacturer = models.TextField(verbose_name='Производитель')
    model = models.TextField(verbose_name='Модель')

    def __str__(self):
        return f'{self.manufacturer} {self.model}'


class Customer(models.Model):
    """Конечные пользователи оборудования"""

    class Meta:
        dv_table = 'customers'
        verbose_name = 'Описание контрагента'
        verbose_name_plural = 'Описание контрагента'

