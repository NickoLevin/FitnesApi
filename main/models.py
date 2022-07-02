from django.db import models
from simple_history.models import HistoricalRecords

class Trainers(models.Model):
    name = models.CharField('Имя', max_length=25)
    surname = models.CharField('Фамилия', max_length=25)
    age = models.IntegerField('Возраст')
    achivments = models.CharField('Достижения', max_length=250)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return f'/trainers_details_view/{self.id}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Abonements(models.Model):
    title = models.CharField('Тип', max_length=25)
    description = models.CharField('Описание', max_length=200)
    price = models.IntegerField('Цена')

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/abonements_details_view{self.id}'


    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'


class Equipments(models.Model):
    equip = models.CharField('Оборудование', max_length=25)
    amount = models.IntegerField('Количество')

    history = HistoricalRecords()

    def __str__(self):
        return self.equip

    def get_absolute_url(self):
        return f'/equipments_details_view{self.id}'

    class Meta:
        verbose_name = 'Тренажер'
        verbose_name_plural = 'Тренажеры'


class Partners(models.Model):
    organisation = models.CharField('Партнер', max_length=100)
    product = models.CharField('Товар', max_length=100)
    contract = models.CharField('Ссылка на сайт', max_length=250)

    history = HistoricalRecords()

    def __str__(self):
        return self.organisation

    def get_absolute_url(self):
        return f'/partners_details_view{self.id}'

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class Clubs(models.Model):
    club_name = models.CharField('Имя клуба', max_length=250)
    location = models.CharField('Местонахождение', max_length=250)
    workin_hours = models.CharField('Рабочие часы', max_length=13)
    date = models.DateField('Дата открытия')

    history = HistoricalRecords()

    def __str__(self):
        return self.club_name

    def get_absolute_url(self):
        return f'/clubs_details_view{self.id}'

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'


class grouptraining(models.Model):
    grouptraining = models.CharField('Груповая тренировка', max_length=250)
    gr_description = models.CharField('Описание тренировки', max_length=250)
    personal = models.ManyToManyField(Trainers, verbose_name='Тренер')
    datetime = models.DateTimeField('Время тренировки')

    history = HistoricalRecords()

    def __str__(self):
        return self.grouptraining

    def get_absolute_url(self):
        return f'/grouptraining_details_view{self.id}'

    class Meta:
        verbose_name = 'Груповая тренировка'
        verbose_name_plural = 'Груповые тренировки'




