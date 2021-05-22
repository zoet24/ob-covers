from django.shortcuts import redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def add_to_bag(request, item_id):
    """ Add quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product.unavailable is True:
        messages.error(request,
                       f'{product.name} is currently unavailable for purchase')
        return redirect(redirect_url)
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request,
                             f'Updated {product.name} quantity in your bag')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Remove the item from the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request,
                         f'Updated {product.name} quantity in your bag')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def bag_to_fav(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        fav = request.session.get('fav', {})
        bag.pop(item_id)
        fav[item_id] = 1
        messages.success(request, f'Added {product.name} to your wish list')

        request.session['bag'] = bag
        request.session['fav'] = fav
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def add_to_fav(request, item_id):
    """ Add 1 of the specified product to the favourites list """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    fav = request.session.get('fav', {})

    if item_id in list(fav.keys()):
        messages.success(request,
                         f'{product.name} is already in your wish list!')
    else:
        fav[item_id] = 1
        messages.success(request, f'Added {product.name} to your wish list')

    request.session['fav'] = fav
    return redirect(redirect_url)


def remove_from_fav(request, item_id):
    """Remove the item from the favourites"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        fav = request.session.get('fav', {})
        fav.pop(item_id)
        messages.success(request,
                         f'Removed {product.name} from your wish list')

        request.session['fav'] = fav
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def fav_to_bag(request, item_id):
    """ Remove the item from the favourites and add to the bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        fav = request.session.get('fav', {})

        if product.unavailable is True:
            messages.error(request,
                           f'{product.name} is currently unavailable.')
            return HttpResponse(status=200)
        else:
            fav.pop(item_id)
            bag[item_id] = 1
            messages.success(request, f'Added {product.name} to your basket')

        request.session['bag'] = bag
        request.session['fav'] = fav
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
