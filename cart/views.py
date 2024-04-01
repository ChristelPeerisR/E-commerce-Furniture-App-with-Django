from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def store(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    try:
        paginated_products = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_products = paginator.page(1)
    except EmptyPage:
        paginated_products = paginator.page(paginator.num_pages)
    return render(request, 'store.html', {'products': paginated_products})

def load_more_products(request):
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 2))
    products = Product.objects.all()[offset:offset+limit]
    products_data = [{'name': product.name} for product in products]
    return JsonResponse({'products': products_data})

def product_list(request):
    products = Product.objects.all()

    # Filter products based on user-selected criteria
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    filter_offer = request.GET.get('offer', None)
    
    if filter_offer == 'true':
        products = products.filter(offer=True)
    if category:
        products = products.filter(category__icontains=category)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, 'product.html', {'products': products, 'category':category, 'min_price':min_price, 'max_price':max_price})

def search(request):
    query = request.GET.get('query')
    products = Product.objects.all()
    pcq = products.filter(category__icontains=query)
    ptq = products.filter(title__icontains=query)
    return render(request, 'search.html', {'products': pcq, 'products': ptq, 'navbar': '#search', 'query': query})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
@login_required
def add(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')
 
def remove(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')