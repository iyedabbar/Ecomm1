from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .cart import Cart
from .models import Order, OrderItem
from django.template.loader import get_template
from django.core.mail import EmailMessage  


def checkout(request, first_name, last_name, email,country, address,city, zipcode, phone, total, amount_to_pay):
    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email,country=country, address=address,city=city, zipcode=zipcode, phone=phone,total=total, amount_to_pay=amount_to_pay)

    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'],  price=item['product'].price, quantity=item['quantity'])


    return order




def notify_customer(order):
    html_tpl_path = 'invoice.html'
    context_data =  {'order': order}
    email_html_template = get_template(html_tpl_path).render(context_data)
    receiver_email = order.email
    
    email_msg = EmailMessage('Welcome from django app', 
                                email_html_template, 
                                settings. DEFAULT_EMAIL_FROM,
                                [receiver_email],
                                reply_to=[settings.DEFAULT_EMAIL_FROM]
                                )
    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)


