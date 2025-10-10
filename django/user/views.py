from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, ListView
from .models import Product, Musician, Album, Brand
from django.views.generic import TemplateView, ListView, DetailView


def product_list(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request: HttpRequest, product_pk: int, product_slug: str) -> HttpResponse:
    product = Product.objects.get(pk=product_pk, slug=product_slug)
    return render(
        request=request,
        template_name='products/product_detail.html',
        context={'product': product},
    )


class IndexPageView(TemplateView):
    template_name = 'index_page.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    pk_url_kwarg = 'product_pk'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'products'


class BrandListView(ListView):
    model = Brand
    template_name = 'products/brand_list.html'
    context_object_name = 'brands'
    ordering = ['name']


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'products/brand_detail.html'
    context_object_name = 'brand'
    pk_url_kwarg = 'pk'
