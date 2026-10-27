
from django.shortcuts import render,get_object_or_404
from .models import Product

def product_list(request):
    search = request.GET.get('search')
    category = request.GET.get('category')

    products = Product.objects.all()

    if search:
        products = products.filter(name__icontains=search)

    if category:
        products = products.filter(category=category)

    categories = Product.objects.values_list(
        'category', flat=True
    ).distinct()

    return render(request, 'list.html', {
        'products': products,
        'categories': categories,
    })



def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {'product': product})