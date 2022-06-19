from django.shortcuts import render, get_object_or_404, redirect

from product.forms import AddToCartForm
from product.models import Product, Category
from cart.cart import Cart


# Create your views here.


def product(request, category_slug, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            # if request.htmx:
            #     return render(request, 'product/partials/addcart.html')
            return redirect('blank', category_slug=category_slug, product_slug=product_slug)

    else:
        form = AddToCartForm()

    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'product/product.html', context)



def blank(request, category_slug, product_slug):

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']


            # if request.htmx:
            #     return redirect('product', category_slug=category_slug, product_slug=product_slug)
            return redirect('blank', category_slug=category_slug, product_slug=product_slug)

    else:
        form = AddToCartForm()

    context = {
        'form': form,
    }
    return render(request, 'product/blank.html', context)


def shop(request):
    # shop = Product.objects.all()
    women = Product.objects.filter(category=1)
    men = Product.objects.filter(category=2)
    bag = Product.objects.filter(category=3)
    shoes = Product.objects.filter(category=4)
    watches = Product.objects.filter(category=5)

    return render(request, 'product/shop.html', {'women': women, 'men': men, 'bag': bag, 'shoes': shoes,
                                                 'watches': watches})


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category': category})
