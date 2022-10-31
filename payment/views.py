from django.contrib import messages
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from . import forms
from django.conf import settings
from payment.forms import CheckoutForm
from .models import Payment


# Create your views here


# def checkout(request):
#     cart = Cart(request)
#
#     if request.method == 'POST':
#         payment_form = forms.CheckoutForm(request.POST)
#         if payment_form.is_valid():
#             payment_form.save()
#
#             cart.clear()
#             return redirect('index')

            # return render(request, 'payment/checkout.html')

        # else:
        #     payment_form = forms.CheckoutForm()
        #
        # return render(request, 'payment/checkout.html', {'payment_form': payment_form})


def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        payment_form = forms.CheckoutForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()

            cart.clear()

            # return redirect('index')

            return render(request, 'payment/confirm_payment.html', {'payment':payment,'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = forms.CheckoutForm()
    return render(request, 'payment/checkout.html', {'payment_form': payment_form})


def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Verification Successful')
    else:
        messages.error(request, 'Verification Failed')
    return redirect('checkout')
