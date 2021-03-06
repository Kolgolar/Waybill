from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib import admin
from django.forms import CheckboxSelectMultiple

class Transport(models.Model): # Справочник транспорта
    id = models.AutoField('№ п/п', primary_key = True)
    mark = models.CharField('Марка, модель', max_length=64)
    year = models.DecimalField('Год выпуска', max_digits = 4, decimal_places = 0, null=True) #Необязательное поле
    plate = models.CharField('Гос. рег. знак', max_length = 16)

    def __str__(self):
        return '{0}'.format(self.id) #Вывод id автобуса

    class Meta:
        verbose_name = 'Автотранспорт ГК "Альтекс"'
        verbose_name_plural = 'Справочник автотранспорта ГК "Альтекс"'


class WRide(models.Model): # Модель поездок
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


class WHead(models.Model): # Модель шапки маршрутных листов
    creation_datetime = models.DateTimeField(null=True)
    date = models.DateTimeField('Дата')
    transport = models.PositiveSmallIntegerField("Транспорт", null = False)

    class Meta:
        verbose_name = 'Заголовок маршрутного листа'
        verbose_name_plural = 'Заголовки маршрутных листов'

    def __str__(self):        
        return 'Создано: {1} | {2}. Заголовок путевого листа №{0}'.format(
            self.id, self.creation_datetime.date(), self.creation_datetime.replace(microsecond=0).time())



class Stop(models.Model): # Справочник остановок (онли названия)
    name = models.CharField('Остановка', max_length = 32)    

    class Meta:
        verbose_name = 'Остановка'
        verbose_name_plural = 'Остановки'

    def __str__(self):
        return self.name


class Route(models.Model): # Модель маршрута
    OUT = 'Вывоз'
    IN = 'Завоз'
    ROUTE_CHOICES = {(OUT, 'Вывоз'),
                     (IN, 'Завоз')}

    num_1 = models.PositiveSmallIntegerField("Индекс", null = False)
    num_2 = models.PositiveSmallIntegerField("Подындекс", null = False)
    description = models.TextField('Описание', max_length=300, blank=True)
    #reverse = models.BooleanField('С конца в начало')
    route_type = models.CharField('Тип поездки', max_length = 5, choices = ROUTE_CHOICES, default = IN)


    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return "{0}/{1}".format(self.num_1, self.num_2)

 #Те же остановки, но уже для отображения в маршруте. Тут какая-то чёрная магия работает:
 # Очень важно не менять порядок объявления в этом скрипте: Stop, Route и InlineStop, иначе полетит всё.
class InlineStop(models.Model):
    name = models.ForeignKey(Stop, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    time = models.TimeField('Время')
    class Meta:
        verbose_name = 'Остановки'
        verbose_name_plural = 'Остановки'

    def __str__(self):
        return str(self.name)


class ExpenseGroup(models.Model): # Справочник групп расходов
    name = models.CharField('Название', max_length = 32)  

    class Meta:
        verbose_name = 'Группа расходов'
        verbose_name_plural = 'Группы расходов'

    def __str__(self):
        return self.name


class Unit(models.Model): # Справочник подразделений
    name = models.CharField('Название', max_length = 32)  

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name