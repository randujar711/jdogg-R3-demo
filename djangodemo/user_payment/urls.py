from django.urls import path 
from . import views 

app_name ='user_payment'

urlpatterns = [
    path('product_page/<int:item_id>/', views.product_page, name='product_page'),
    path('payment_succesful/', views.payment_successful, name='payment_successful/'),
    path('payment_cancelled/', views.payment_cancelled, name='payment_cancelled/'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook')
]