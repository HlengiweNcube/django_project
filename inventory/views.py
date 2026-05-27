from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

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
@permission_required('inventory.add_product', raise_exception=True)
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
@permission_required('inventory.change_product', raise_exception=True)
def update_product(request, product_id):

    product = get_object_or_404(Product, id=product_id)

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
@permission_required('inventory.delete_product', raise_exception=True)
def delete_product(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    product.delete()

    return redirect('product_list')