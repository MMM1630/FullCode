# Generated by Django 5.2.2 on 2025-06-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullcode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolcontact',
            name='choices',
            field=models.CharField(choices=[('Python', 'Python'), ('JavaScript', 'JavaScript')], default='Вопросы по курсу', max_length=30, verbose_name='Выбор'),
        ),
        migrations.AlterField(
            model_name='comands',
            name='positon',
            field=models.CharField(max_length=30, verbose_name='Должность'),
        ),
    ]
