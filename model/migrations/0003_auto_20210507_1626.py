# Generated by Django 3.1.5 on 2021-05-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_auto_20210507_1319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': ('Заказ',), 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(default=None, null=True, verbose_name='Краткое описание*'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(default=None, max_length=255, null=True, verbose_name='Электронный адрес*'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='Ваше ФИО*'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phonenumber',
            field=models.CharField(default=None, max_length=25, null=True, verbose_name='Номер телефона*'),
        ),
    ]
