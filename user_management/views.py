from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from inventory.models import Product
from imports.models import ImportRecord
from exports.models import ExportRecord

from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

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

            return redirect('dashboard')

    else:
        form = AuthenticationForm()

    return render(request, 'user_management/login.html', {'form': form})


@login_required
def dashboard_view(request):

    total_products = Product.objects.count()

    total_imports = ImportRecord.objects.count()

    total_exports = ExportRecord.objects.count()

    low_stock_products = Product.objects.filter(
        quantity__lt=10
    )

    context = {

        'total_products': total_products,

        'total_imports': total_imports,

        'total_exports': total_exports,

        'low_stock_products': low_stock_products,
    }

    return render(
        request,
        'user_management/dashboard.html',
        context
    )


def logout_view(request):
    logout(request)

    return redirect('login')