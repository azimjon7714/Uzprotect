from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', base_view, name="base"),
    re_path(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name="category_detail"),
    re_path(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name="product_detail")
]
