from django import forms
from django.forms import ModelForm

from .models import Payment


class CheckoutForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['full_name', 'email', 'phone', 'address', 'amount']



