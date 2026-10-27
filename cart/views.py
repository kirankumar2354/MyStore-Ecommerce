
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import CartItem
from orders.models import Order


@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product_list')




@login_required
def cart_list(request):
    items = CartItem.objects.filter(user=request.user)

    total = 0

    for item in items:
        total += item.product.price * item.quantity

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })


@login_required
def remove_from_cart(request, id):
    item = get_object_or_404(
        CartItem,
        id=id,
        user=request.user
    )
    item.delete()
    return redirect('cart_list')



@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)

    if not items.exists():
        return redirect('cart_list')

    total = sum(item.product.price * item.quantity for item in items)

    if request.method == 'POST':
        Order.objects.create(
            user=request.user,
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            total=total
        )

        items.delete()
        return redirect('my_orders')

    return render(request, 'checkout.html', {
        'items': items,
        'total': total
    })
