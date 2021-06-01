from django.db import models
from django.urls import reverse


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class ModelTxt(models.Model):
    # model = models.ForeignKey(AboutModels, verbose_name='Модель', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=50, default=None)
    file = models.FileField(verbose_name='Файл модели', upload_to='upload_to/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл модели',
        verbose_name_plural = 'Файлы Моделей'


class TechologyTask(models.Model):
    # model = models.ForeignKey(AboutModels, verbose_name='Модель', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=50, default=None)
    file = models.FileField(verbose_name='Файл технического описания', upload_to='upload_to/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Техническое описание',
        verbose_name_plural = 'Технические описания'


class Type(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип',
        verbose_name_plural = 'Типы'


class EnviromentalCondition(models.Model):
    Condition = models.CharField(max_length=50, verbose_name='Условие', default=None, null=True)

    def __str__(self):
        return self.Condition

    class Meta:
        verbose_name = 'Условие эксплуатации',
        verbose_name_plural = 'Условия эксплуатации'


# class ModelTxtOnline(models.Model):
#     model = models.ForeignKey(AboutModels, verbose_name='Модель', on_delete=models.CASCADE)
#     link = models.CharField(max_length=255, verbose_name='Ссылка на файл')

class AboutModels(models.Model):
    class Meta:
        abstract = True

    type = models.ForeignKey(Type, verbose_name='Категория', on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField('Название', max_length=50, default=None)
    function = models.CharField('Производитель', max_length=50, default=None)
    basicModel = models.CharField('Макс. мощность, Вт', max_length=50, default=None)
    body = models.CharField('Корпус', max_length=50, default=None)
    down = models.ForeignKey(ModelTxt, verbose_name='Файл модели', on_delete=models.CASCADE)
    technicaldescription = models.ForeignKey(TechologyTask, verbose_name='Файл технического описания',
                                             on_delete=models.CASCADE)
    conditions = models.ForeignKey(EnviromentalCondition, verbose_name='Условия эксплуатации', on_delete=models.CASCADE,
                                   default=None, null=True)
    ready = models.BooleanField(verbose_name='Открытый доступ', default=True)

    # down = models.FileField('Файл модели', upload_to='model/', default=None, null=True)

    def __str__(self):
        return self.title


class Diod(AboutModels):
    maxcurrent = models.CharField('Максимальный ток, А', max_length=255)
    maxvoltage = models.CharField('Максимальное напряжение, В', max_length=255)
    breakdownvoltage = models.CharField('Напряжение пробоя, В', max_length=255)

    def __str__(self):
        return "{} : {}".format(self.type.name, self.title)

    class Meta:
        verbose_name = 'Диод',
        verbose_name_plural = 'Диоды'


class TransistorBP(AboutModels):
    maxcurrent = models.CharField('Максимальный ток коллектора , А', max_length=255)
    maxvoltage = models.CharField('Максимальное напряжение коллектор-эмитер, В', max_length=255)

    def __str__(self):
        return "{} : {}".format(self.type.name, self.title)

    class Meta:
        verbose_name = 'Биполярный транзистор',
        verbose_name_plural = 'Биполярные транзисторы'


class TransistorPOLEV(AboutModels):
    maxcurrent = models.CharField('Максимальный ток стока, А', max_length=255)
    maxvoltageSI = models.CharField('Максимальное напряжение сток-истока, В', max_length=255)
    maxvoltageZI = models.CharField('Максимальное напряжение затвор-исток, В', max_length=255)

    def __str__(self):
        return "{} : {}".format(self.type.name, self.title)

    class Meta:
        verbose_name = 'Полевой транзистор',
        verbose_name_plural = 'Полевые транзисторы'


class Order(models.Model):

    name = models.CharField('Ваше ФИО*', max_length=50, default=None, null=True)
    email = models.EmailField('Электронный адрес*', max_length=255, default=None, null=True)
    phonenumber = models.CharField('Номер телефона*', max_length=25, default=None, null=True)
    description = models.TextField('Краткое описание*', default=None, null=True)

    def __str__(self):
        return "{} : {}".format(self.name, self.email)

    class Meta:
        verbose_name = 'Заказ',
        verbose_name_plural = 'Заказы'


# class TableModels(models.Model):
#     number = models.IntegerField('Номер')
#     function_m = models.CharField('Производитель', max_length=50, default=1)
#     basicModel_m = models.IntegerField('Макс. Допустимый ток, А')
#     structure_m = models.TextField('Структура', max_length=50, default=1)
#     body_m = models.CharField('Корпус', max_length=50, default='npn')
#
#     def __str__(self):
#         return self.title
#     class Meta:
#         verbose_name = 'Таблица',
#         verbose_name_plural = 'Таблицы'
