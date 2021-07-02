from django.db import models

class WayBill(models.Model):
    date = models.DateTimeField('Дата')
    transport = models.IntegerField('Номер ТС')
    time_in = models.TimeField('Время прибытия')
    time_out = models.TimeField('Время убытия')
    route = models.CharField('Маршрут', max_length=5)
    expense_group = models.CharField('Группа расходов', max_length = 32)
    unit = models.CharField('Подразделение', max_length = 32)

    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Маршрутный лист'
        verbose_name_plural = 'Маршрутные листы'