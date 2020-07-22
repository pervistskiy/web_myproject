# Generated by Django 3.0.8 on 2020-07-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Отчество')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('country', models.CharField(max_length=40, verbose_name='Страна')),
                ('group', models.IntegerField(verbose_name='Номер группы')),
                ('course', models.IntegerField(blank=True, null=True, verbose_name='Номер курса')),
                ('telephone', models.CharField(blank=True, max_length=13, null=True, verbose_name='Номер телефона')),
                ('specialty', models.CharField(max_length=100, verbose_name='Специальность')),
                ('form_group', models.CharField(max_length=20, verbose_name='Форма обучения')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]