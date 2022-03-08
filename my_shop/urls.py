# my_shop/urls.py
# Django modules
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from stripe_shop.views import create_stripe_checkout_session, stripe_webhook_paid_endpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='shop.html')),
    path('create-checkout-session/<str:product_name>', create_stripe_checkout_session),
    path('stripe-webhook-paid/', stripe_webhook_paid_endpoint),
]
