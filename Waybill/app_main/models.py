from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib import admin
from django.forms import CheckboxSelectMultiple, MultiWidget

class Transport(models.Model):
    id = models.AutoField('№ п/п', primary_key = True)
    mark = models.CharField('Марка, модель', max_length=64)
    year = models.DecimalField('Год выпуска', max_digits = 4, decimal_places = 0, null=True) #Необязательное поле
    plate = models.CharField('Гос. рег. знак', max_length = 16)

    def __str__(self):
        return '{0}'.format(self.id) #Вывод id автобуса

    class Meta:
        verbose_name = 'Автотранспорт ГК "Альтекс"'
        verbose_name_plural = 'Справочник автотранспорта ГК "Альтекс"'


class WRide(models.Model):
    head_id = models.PositiveIntegerField('№')
    time_in = models.TimeField('Время при прибытии')
    time_out = models.TimeField('Время при убытии')
    route = models.CharField('Маршрут', max_length=5)
    expense_group = models.CharField('Группа расходов', max_length = 32)
    unit = models.CharField('Подразделение', max_length = 32)

    
    def __str__(self):
        return 'Поездка №{0}, путевой лист №{1}'.format(self.id, self.head_id)    

    class Meta:
        verbose_name = 'Поездка маршрутного листа'
        verbose_name_plural = 'Поездки маршрутных листов'


class WHead(models.Model):
    creation_datetime = models.DateTimeField(null=True)
    date = models.DateTimeField('Дата')
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Заголовок маршрутного листа'
        verbose_name_plural = 'Заголовки маршрутных листов'

    def __str__(self):        
        return 'Создано: {1} | {2}. Заголовок путевого листа №{0}'.format(
            self.id, self.creation_datetime.date(), self.creation_datetime.replace(microsecond=0).time())



class Stop(models.Model):
    name = models.CharField('Остановка', max_length = 32)

    class Meta:
        verbose_name = 'Остановка'
        verbose_name_plural = 'Остановки'

    def __str__(self):
        return self.name


class Route(models.Model):
    num = models.CharField('Номер', max_length=5)
    stops = models.ManyToManyField(Stop)


    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
    



class AdminRouteModel(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': MultiWidget}}