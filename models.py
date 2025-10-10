from decimal import Decimal
from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва бренду")
    country = models.CharField(max_length=100, verbose_name="Країна")
    description = models.TextField(verbose_name="Опис")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренди"


class Musician(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} - {self.musician.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=255)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(default=Decimal('0.0'), max_digits=2, decimal_places=1)

    def get_absolute_url(self):
        return reverse(
            "product_detail", kwargs={"product_pk": self.pk, "product_slug": self.slug}
        )
