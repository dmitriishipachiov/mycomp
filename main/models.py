from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name='URL')
    

    class Meta:
        db_table: 'Category'
        verbose_name='Категорию'
        verbose_name_plural='Категории'


    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='main_images', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, verbose_name='Категория')


    class Meta:
        db_table: 'Post'
        verbose_name='Пост'
        verbose_name_plural='Посты'


    def __str__(self):
        return self.title
    