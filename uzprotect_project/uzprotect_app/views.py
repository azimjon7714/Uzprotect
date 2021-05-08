from django.shortcuts import render
from .models import *

def base_view(request):
    categories = Category.objects.all()
    about_us = AboutUs.objects.all()

    context = {
        'categories': categories,
        'about_us': about_us,
    }
    return render(request, 'index.html', context)

def category_view(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products_by_category = Product.objects.filter(category=category)

    context = {
        'categories': categories,
        'category': category,
        'products_by_category': products_by_category,
    }
    return render(request, 'area.html', context)

def product_view(request, product_slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)

    context = {
        'categories': categories,
        'product': product,
    }
    return render(request, 'product.html', context)
# Create your views here.
