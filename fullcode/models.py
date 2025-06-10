# Айти разработка
from django.db import models

class ProjectContact(models.Model):
    name = models.CharField("Имя",max_length=30)
    phone_number = models.CharField("Номер телефона", max_length=30)
    text = models.TextField("Текст сообщения")

    class Meta:
        verbose_name = "Контакт для проекта"
        vrebose_name_plural = "Контакты для проектов"


class Services(models.Model):
    term = models.CharField("Услуга", max_length=30)
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание услуги")
    img = models.ImageField("Изоброжение")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Progect(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    img = models.ImageField("Изоброжение")

    class Meta:
        verbose_name = "Наши проекты"
        verbose_name_plural = "Наши проекты"


class Comands(models.Model):
    name = models.CharField("ФИО", max_length=50)
    positon = models.CharField("Должеость", max_length=30)
    img = models.ImageField("Фотография")

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"


# Айти школа

class SchoolContact(models.Model):
    name = models.CharField("Имя",max_length=30)
    phone_number = models.CharField("Номер телефона", max_length=30)
    text = models.TextField("Текст сообщения")

    class Meta:
        verbose_name = "Контакты для учащихся"
        vrebose_name_plural = "Контакты для учащихся"


class Courses(models.Model):
    name = models.CharField("Направелиние курса", max_length=50)
    title = models.CharField("Заголовок", max_length=100)
    discount = models.CharField("Скидка", max_length=10, null=True, blank=True)
    launch = models.DateField("Запуск курса")
    duration = models.CharField("Длительность курса", max_length=30)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

class Pros(models.Model):
    trainees = models.CharField("Стажеры", max_length=30)
    mentors = models.CharField("Менторы", max_length=30)
    graduates = models.CharField("Выпускники", max_length=100)
# Подарки от компании
    img = models.ImageField("Изоброжение")
    title = models.CharField("Загаловок", max_length=100)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "Преимущества"
        verbose_name_plural = "Преимущества"


class Certificates(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    img = models.ImageField("Изоброжение")

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"