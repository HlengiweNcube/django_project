from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Product, Project
from .forms import ProductForm, ProjectForm


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
            messages.success(request, 'Product created successfully.')

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
            messages.success(request, 'Product updated successfully.')

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
    messages.success(request, 'Product deleted successfully.')

    return redirect('product_list')


@login_required
def project_list(request):

    projects = Project.objects.filter(owner=request.user).order_by('-created_at')
    status_filter = request.GET.get('status', '').strip()

    if status_filter:
        projects = projects.filter(status=status_filter)

    return render(
        request,
        'inventory/project_list.html',
        {
            'projects': projects,
            'status_filter': status_filter,
            'status_choices': Project.STATUS_CHOICES,
        }
    )


@login_required
@permission_required('inventory.add_project', raise_exception=True)
def add_project(request):

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, 'Project added successfully.')

            return redirect('project_list')

    else:
        form = ProjectForm()

    return render(
        request,
        'inventory/add_project.html',
        {'form': form}
    )


@login_required
@permission_required('inventory.change_project', raise_exception=True)
def update_project(request, project_id):

    project = get_object_or_404(Project, id=project_id, owner=request.user)

    if request.method == 'POST':

        form = ProjectForm(
            request.POST,
            instance=project
        )

        if form.is_valid():

            form.save()
            messages.success(request, 'Project updated successfully.')

            return redirect('project_list')

    else:

        form = ProjectForm(instance=project)

    return render(
        request,
        'inventory/update_project.html',
        {'form': form, 'project': project}
    )