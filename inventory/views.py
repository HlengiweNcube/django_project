from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm


@login_required
def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        'inventory/product_list.html',
        {'products': products}
    )


@login_required
def add_product(request):

    if request.method == 'POST':

        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('product_list')

    else:

        form = ProductForm()

    return render(
        request,
        'inventory/add_product.html',
        {'form': form}
    )


@login_required
def update_product(request, product_id):

    product = Product.objects.get(id=product_id)

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            instance=product
        )

        if form.is_valid():

            form.save()

            return redirect('product_list')

    else:

        form = ProductForm(instance=product)

    return render(
        request,
        'inventory/update_product.html',
        {'form': form}
    )


@login_required
def delete_product(request, product_id):

    product = Product.objects.get(id=product_id)

    product.delete()

    return redirect('product_list')