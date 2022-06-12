# from cart.cart import Cart
#
# from django.conf import settings
# # for HTML Email
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
#
# from .models import Payment
#
#
# def checkout(request, full_name, email, phone, address, amount):
#     payment = Payment.objects.create(full_name=full_name, email=email, phone=phone, address=address,
#                                      amount=amount)
#
#     for item in Cart(request):
#         OrderItem.objects.create(payment=payment, product=item['product'],
#                                  price=item['product'].price, quantity=item['quantity'])
#         payment.add(item['product'])
#
#     return payment
#
#
# # def notify_vendor(order):
# #     from_email = settings.DEFAULT_EMAIL_FROM
# #
# #     for vendor in order.vendors.all():
# #         to_email = vendor.created_by.email
# #         subject = 'New order'
# #         text_content = 'You have a new order!'
# #         html_content = render_to_string('order/email_notify_vendor.html', {'order': order, 'vendor': vendor})
# #
# #         msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
# #         msg.attach_alternative(html_content, 'text/html')
# #         msg.send()
#
#
# def notify_customer(order):
#     from_email = settings.DEFAULT_EMAIL_FROM
#
#     to_email = order.email
#     subject = 'Order confirmation'
#     text_content = 'Thank you for the order!'
#     html_content = render_to_string('order/email_notify_customer.html', {'order': order})
#
#     msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
