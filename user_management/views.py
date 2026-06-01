from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from inventory.models import Product
from inventory.models import Project
from imports.models import ImportRecord
from exports.models import ExportRecord

from .forms import RegisterForm, UpdateProfileForm, UpdateContactForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            staff_group, _ = Group.objects.get_or_create(name='Staff')
            user.groups.add(staff_group)
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')

            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(request, 'user_management/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}.')

            return redirect('dashboard')

    else:
        form = AuthenticationForm()

    return render(request, 'user_management/login.html', {'form': form})


@login_required
def dashboard_view(request):

    total_products = Product.objects.count()

    total_imports = ImportRecord.objects.count()

    total_exports = ExportRecord.objects.count()

    total_projects = Project.objects.filter(owner=request.user).count()

    low_stock_products = Product.objects.filter(
        quantity__lt=10
    )

    context = {

        'total_products': total_products,

        'total_imports': total_imports,

        'total_exports': total_exports,

        'total_projects': total_projects,

        'low_stock_products': low_stock_products,
    }

    return render(
        request,
        'user_management/dashboard.html',
        context
    )


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')

    return redirect('login')

@login_required
def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':

        form = UpdateProfileForm(
            request.POST,
            instance=request.user
        )
        contact_form = UpdateContactForm(
            request.POST,
            instance=profile
        )

        if form.is_valid() and contact_form.is_valid():

            form.save()
            contact_form.save()
            messages.success(request, 'Profile and contact details updated.')

            return redirect('dashboard')

    else:

        form = UpdateProfileForm(
            instance=request.user
        )
        contact_form = UpdateContactForm(instance=profile)

    return render(
        request,
        'user_management/update_profile.html',
        {
            'form': form,
            'contact_form': contact_form,
        }
    )