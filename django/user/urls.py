from django.urls import path
from .views import product_list, product_detail, IndexPageView, ProductListView, ProductDetailView, AboutPageView, \
    BrandDetailView, BrandListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:product_pk>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('brands/', BrandListView.as_view(), name='brand_list'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand_detail'),
]
