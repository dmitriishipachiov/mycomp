from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name='URL')


    class Meta:
        db_table: 'Category'
        verbose_name='Категорию'
        verbose_name_plural='Категории'


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    cuanlity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='static.images', blank=True, null=True, verbose_name='Изображение')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name='URL')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, verbose_name='Категория')


    class Meta:
        db_table: 'Product'
        verbose_name='Продукт'
        verbose_name_plural='Продукты'
