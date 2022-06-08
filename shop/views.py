from django.shortcuts import render
from product.models import Category, Product


# Create your views here.


def index(request):
    category = Category.objects.all()[0:2]
    accessories_product = Product.objects.filter(type="Accessories")
    # products = Product.objects.all()
    women = Product.objects.filter(category=1)
    men = Product.objects.filter(category=2)
    bag = Product.objects.filter(category=3)
    shoes = Product.objects.filter(category=4)
    watches = Product.objects.filter(category=5)

    return render(request, 'shop/index.html', {'category': category, 'accessories_product': accessories_product,
                                               'women': women, 'men': men, 'bag': bag, 'shoes': shoes,
                                               'watches': watches})
