from django.contrib import admin
from .models import Product, Brand, Musician, Album


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price')
    list_filter = ('available', 'created', 'updated')
    search_fields = ('name', 'description')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'instrument')
    list_filter = ('instrument',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'musician', 'release_year', 'genre')
    list_filter = ('genre', 'release_year')
    search_fields = ('title', 'musician__name')
