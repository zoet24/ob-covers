from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Colour


def bag_contents(request):
    # Context for shopping basket
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    products_available = True

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
        if product.unavailable is True:
            products_available = False

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'products_available': products_available,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context


def fav_contents(request):
    # Context for wish list
    fav_items = []
    product_count_fav = 0
    fav = request.session.get('fav', {})

    for item_id, quantity in fav.items():
        product = get_object_or_404(Product, pk=item_id)
        product_count_fav += quantity
        fav_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'fav_items': fav_items,
        'product_count_fav': product_count_fav,
    }

    return context


def cover_swatches(request):
    # Context for cover swatches across site
    products_swatch = Product.objects.all()

    classic_products = products_swatch.filter(range__name="classic").order_by('?')
    classic_swatch = []
    classic_colours = []

    for product in classic_products:
        if product.colour.name not in classic_colours:
            classic_colours.append(product.colour.name)
            classic_swatch.append(product)

    stylish_products = products_swatch.filter(range__name="stylish").order_by('?')
    stylish_swatch = []
    stylish_colours = []

    for product in stylish_products:
        if product.colour.name not in stylish_colours:
            stylish_colours.append(product.colour.name)
            stylish_swatch.append(product)

    premium_products = products_swatch.filter(range__name="premium").order_by('?')
    premium_swatch = []
    premium_colours = []
    premium_styles = []

    for product in premium_products:
        if product.colour.name not in premium_colours or product.style.name not in premium_styles:
            premium_colours.append(product.colour.name)
            premium_styles.append(product.style.name)
            premium_swatch.append(product)

    disney_products = products_swatch.filter(range__name="disney").order_by('?')
    disney_swatch = []
    disney_colours = []
    disney_styles = []

    for product in disney_products:
        if product.colour.name not in disney_colours or product.style.name not in disney_styles:
            disney_colours.append(product.colour.name)
            disney_styles.append(product.style.name)
            disney_swatch.append(product)

    swatch_context = {
        'classic_swatch': classic_swatch,
        'stylish_swatch': stylish_swatch,
        'premium_swatch': premium_swatch,
        'disney_swatch': disney_swatch,
        'products_swatch': products_swatch,
    }

    return swatch_context
