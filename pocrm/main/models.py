from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Kroy(models.Model):
    class Meta:
            verbose_name = ('Крой')
    name = models.CharField(max_length=250, verbose_name='Наименование')
    kroy_no = models.IntegerField(verbose_name='Крой номер')
    ras_tkani = models.FloatField(verbose_name='Расход ткани')
    ras_dublerin = models.FloatField(verbose_name='Расход дублерин')
    edinitsa = models.IntegerField(null=True, blank=True, verbose_name='Единица')
    description = models.TextField(null=True, blank=True, verbose_name='Примечение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def update_edinitsa(self):
        # Calculate the sum of stuk from related Kroy_detail objects
        total_stuk = self.kroy_detail_set.aggregate(total_stuk=models.Sum('stuk'))['total_stuk']

        if total_stuk is not None:
            # Add the sum to the edinitsa field
            self.edinitsa = self.edinitsa + total_stuk
            self.save()

    def __str__(self):
        return str(self.kroy_no)

class Kroy_detail(models.Model):
    class Meta:
            verbose_name = ('Крой детально')
    kroy = models.ForeignKey(Kroy, on_delete=models.CASCADE, verbose_name='Крой')
    pachka = models.CharField(max_length=200, verbose_name='Пачка')
    razmer = models.CharField(max_length=200, verbose_name='Размер')
    rost = models.CharField(max_length=200, verbose_name='Рост')
    stuk = models.IntegerField(verbose_name='Штук')


    def __str__(self):
        return self.pachka


class Uchastok(models.Model):
    class Meta:
            verbose_name = ('Участок')
    name = models.CharField(max_length=150, verbose_name='Участок')

    def __str__(self):
        return self.name

class Masterdata(models.Model):
    class Meta:
            verbose_name = ('Общая таблица')
    kroy_no = models.IntegerField(verbose_name='Крой номер')
    status = models.CharField(max_length=50, verbose_name='Статус')
    edinitsa = models.IntegerField(verbose_name='Единица')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    description = models.TextField(null=True, blank=True, verbose_name='Примечение')


