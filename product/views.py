from django.shortcuts import render, get_object_or_404

from product.models import Product, Category

# Create your views here.


def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    return render(request, 'product/product.html', {'product': product})


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category': category})
