from django.db import models

class Transport(models.Model):
    id = models.AutoField('№ п/п', primary_key = True)
    mark = models.CharField('Марка, модель', max_length=64)
    year = models.DecimalField('Год выпуска', max_digits = 4, decimal_places = 0, null=True) #Необязательное поле
    plate = models.CharField('Гос. рег. знак', max_length = 16)

    def __str__(self):
        return '{}'.format(self.id) #Вывод id автобуса

    class Meta:
        verbose_name = 'Автотранспорт ГК "Альтекс"'
        verbose_name_plural = 'Справочник автотранспорта ГК "Альтекс"'

class WRide(models.Model):
    time_in = models.TimeField('Время прибытия')
    time_out = models.TimeField('Время убытия')
    route = models.CharField('Маршрут', max_length=5)
    expense_group = models.CharField('Группа расходов', max_length = 32)
    unit = models.CharField('Подразделение', max_length = 32)

    
    def __str__(self):
        return self.route

    class Meta:
        verbose_name = 'Поездка маршрутного листа'
        verbose_name_plural = 'Поездки маршрутных листов'

class WHead(models.Model):
    #id = models.AutoField('№', primary_key = True)
    date = models.DateTimeField('Дата')
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Заголовок маршрутного листа'
        verbose_name_plural = 'Заголовки маршрутных листов'