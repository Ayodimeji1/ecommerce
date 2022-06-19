from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from ecommerce.settings import dev
from . import forms
from .forms import CheckoutForm

from .models import Payment
# Create your views here


def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        payment_form = forms.CheckoutForm(request.POST)
        if payment_form.is_valid():
            payment_form.save()

            cart.clear()

            return redirect('index')

            # return render(request, 'payment/checkout.html',
            #               {'payment': payment, 'FLUTTERWAVE_PUBLIC_KEY': dev.FLUTTERWAVE_PUBLIC_KEY})



    else:
        payment_form = forms.CheckoutForm()

    return render(request, 'payment/checkout.html', {'payment_form': payment_form})



# def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
#     payment = get_object_or_404(Payment, ref=ref)
#     verified = payment.verify_payment()
#     if verified:
#         messages.success(request, 'Verification Successful')
#     else:
#         messages.error(request, 'Verification Failed')
#     return redirect('index')
