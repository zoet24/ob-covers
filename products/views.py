from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Range, Colour, Style
from .forms import ProductForm


def all_products(request):
    # A view to show all products, including sorting and search queries
    product = None
    products = Product.objects.all()

    colour_choices = Colour.objects.all()
    style_choices = Style.objects.all()
    range_choices = Range.objects.all()

    colours_array = []
    styles_array = []
    ranges_array = []

    available_num = products.filter(unavailable=False).count()
    unavailable_num = products.filter(unavailable=True).count()
    other_num = 0

    for colour in colour_choices:
        num = products.filter(colour__name=colour).count()
        colour_array = ({"name": colour.name,
                         "friendly_name": colour.friendly_name,
                         "count": num})
        colours_array.append(colour_array)

    for style in style_choices:
        num = products.filter(style__name=style).count()
        style_array = ({"name": style.name,
                        "friendly_name": style.friendly_name,
                        "count": num})
        styles_array.append(style_array)

    for range in range_choices:
        num = products.filter(range__name=range).count()
        range_array = ({"name": range.name,
                        "friendly_name": range.friendly_name,
                        "count": num})
        ranges_array.append(range_array)

    query = None
    range = None
    ranges = None
    style = None
    styles = None
    colour = None
    colours = None
    current_other = None
    sort = None
    direction = None
    current_sorting = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'range':
                sortkey = 'range__name'
            if sortkey == 'style':
                sortkey = 'style__name'
            if sortkey == 'colour':
                sortkey = 'colour__friendly_name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            current_sorting = f'{sort}_{direction}'

        if 'range' in request.GET:
            ranges = request.GET['range'].split(',')
            products = products.filter(range__name__in=ranges)
            ranges = Range.objects.filter(name__in=ranges)
            if ranges:
                range = ranges[0]

        if 'style' in request.GET:
            styles = request.GET['style'].split(',')
            products = products.filter(style__name__in=styles)
            styles = Style.objects.filter(name__in=styles)
            if styles:
                style = styles[0]

        if 'colour' in request.GET:
            colours = request.GET['colour'].split(',')
            products = products.filter(colour__name__in=colours)
            colours = Colour.objects.filter(name__in=colours)
            if colours:
                colour = colours[0]

        if 'other' in request.GET:
            other = request.GET['other'].split('is')[0]
            other_value = request.GET['other'].split('is')[1]
            if other_value == "true":
                other_value = True
            else:
                other_value = False
            if other == "unavailable":
                products = products.filter(unavailable=other_value)
                other_num = products.filter(unavailable=other_value).count()
                if other_value is True:
                    current_other = "Unavailable"
                else:
                    current_other = "Available"

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'product': product,
        'products': products,
        'available_num': available_num,
        'unavailable_num': unavailable_num,
        'other_num': other_num,
        'colours': colours_array,
        'styles': styles_array,
        'ranges': ranges_array,
        'search_term': query,
        'current_range': range,
        'current_style': style,
        'current_colour': colour,
        'current_other': current_other,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    # A view to show individual product details

    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()
    colours = Colour.objects.all()

    context = {
        'product': product,
        'products': products,
        'colours': colours,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product. '
                           'Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product. '
                           'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product_id_str = str(product_id)

    bag = request.session.get('bag', {})
    fav = request.session.get('fav', {})
    if product_id_str in list(bag.keys()):
        bag.pop(product_id_str)
    if product_id_str in list(fav.keys()):
        fav.pop(product_id_str)

    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
