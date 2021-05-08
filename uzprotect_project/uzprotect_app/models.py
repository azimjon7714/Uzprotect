from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название сферы деятельности")
    slug = models.SlugField(verbose_name="Альтернативное название")

    class Meta:
        verbose_name = "Сфера деятельность"
        verbose_name_plural = "Сфера деятельности"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})

def image_folder(instance, filename):
    filename = instance.slug + "." + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

class Product(models.Model):
    category = models.ForeignKey(
                            Category,
                            on_delete=models.CASCADE,
                            verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    slug = models.SlugField(verbose_name="Альтернативное название")
    description = models.TextField(verbose_name="Описание продукта")
    price = models.PositiveIntegerField(verbose_name="Цена продукта")
    image = models.ImageField(upload_to=image_folder, verbose_name="Картинка продукта")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return "{0}-{1}".format(self.category, self.name)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

class AboutUs(models.Model):
    activity = models.TextField(verbose_name="Наша деятельность")

    class Meta:
        verbose_name = "Наша деятельность"
        verbose_name_plural = "Наши деятельности"

    def __str__(self):
        return self.activity