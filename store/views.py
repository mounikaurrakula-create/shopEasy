from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def home(request):
    return render(request, 'store/home.html')


def products(request):
    products = Product.objects.all()

    return render(
        request,
        'store/products.html',
        {
            'products': products
        }
    )


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        'store/product_detail.html',
        {
            'product': product
        }
    )


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def cart(request):
    cart_data = request.session.get('cart', {})

    cart_items = []
    total = 0

    for product_id, quantity in cart_data.items():

        product = get_object_or_404(Product, id=product_id)

        subtotal = product.price * quantity

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

        total += subtotal

    return render(
        request,
        'store/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


def increase_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def decrease_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] -= 1

        if cart[product_id_str] <= 0:
            del cart[product_id_str]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id_str = str(product_id)

    if product_id_str in cart:
        del cart[product_id_str]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')