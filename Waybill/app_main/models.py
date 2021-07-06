from django.db import models

class Transport(models.Model):
    id = models.DecimalField('№ п/п', max_digits = 3, decimal_places = 0, primary_key = True)
    mark = models.CharField('Марка, модель', max_length=64)
    year = models.DecimalField('Год выпуска', max_digits = 4, decimal_places = 0, null=True) #Необязательное поле
    plate = models.CharField('Гос. рег. знак', max_length = 16)

    def __str__(self):
        return self.plate

    class Meta:
        verbose_name = 'Автотранспорт ГК "Альтекс"'
        verbose_name_plural = 'Справочник автотранспорта ГК "Альтекс"'

class WayBill(models.Model):
    date = models.DateTimeField('Дата')
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True)
    time_in = models.TimeField('Время прибытия')
    time_out = models.TimeField('Время убытия')
    route = models.CharField('Маршрут', max_length=5)
    expense_group = models.CharField('Группа расходов', max_length = 32)
    unit = models.CharField('Подразделение', max_length = 32)

    

    
    def __str__(self):
        return self.route

    class Meta:
        verbose_name = 'Маршрутный лист'
        verbose_name_plural = 'Маршрутные листы'

