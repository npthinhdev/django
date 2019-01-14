from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from products.models import Product
from shopping_cart.models import OrderItem, Order
from shopping_cart.extras import generate_order_id

def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0

@login_required()
def add_to_cart(request, pk):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = Product.objects.filter(pk=pk).first()
    if product in request.user.profile.ebooks.all():
        messages.info(request, 'You already own this ebook')
        return redirect(reverse('products:product_list'))
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
    messages.info(request, 'item added to cart')
    return redirect(reverse('products:product_list'))

@login_required()
def delete_from_cart(request, pk):
    item_to_delete = OrderItem.objects.filter(pk=pk)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, 'Item has been deleted')
    return redirect(reverse('shopping_cart:order_summary'))

@login_required()
def order_details(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)

@login_required()
def checkout(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/checkout.html', context)

@login_required()
def process_payment(request, pk):
    return redirect(reverse('shopping_cart:update_records', args=[pk]))

@login_required()
def update_transaction_records(request, pk):
    order_to_purchase = Order.objects.filter(pk=pk).first()
    order_to_purchase.is_ordered = True
    order_to_purchase.date_ordered = datetime.now()
    order_to_purchase.save()

    order_items = order_to_purchase.items.all()
    order_items.update(is_ordered=True, date_ordered=datetime.now())

    user_profile = get_object_or_404(Profile, user=request.user)
    order_products = [item.product for item in order_items]
    user_profile.ebooks.add(*order_products)
    user_profile.save()

    messages.info(request, 'Thank you! Your purchase was successful!')
    return redirect(reverse('accounts:my_profile'))

def success(request):
    return render(request, 'shopping_cart/purchase_success.html')
