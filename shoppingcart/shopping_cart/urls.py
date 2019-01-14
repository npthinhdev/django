from django.urls import path
from . import views

app_name = 'shopping_cart'

urlpatterns = [
    path('add-to-cart/<int:pk>', views.add_to_cart, name='add-to-cart'),
    path('order-summary/', views.order_details, name='order_summary'),
    path('success/', views.success, name='purchase_success'),
    path('item/delete/<int:pk>', views.delete_from_cart, name='delete_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('update-transaction/<int:pk>', views.update_transaction_records, name='update_records')
]
