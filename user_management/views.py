from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.http import FileResponse, Http404
from django.utils import timezone
from django.db.models import Sum, DecimalField, Value
from django.db.models.functions import Coalesce
from pathlib import Path
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
            display_name = user.get_full_name().strip() or user.username
            messages.success(request, f'Welcome back, {display_name}.')

            return redirect('dashboard')

    else:
        form = AuthenticationForm()

    return render(request, 'user_management/login.html', {'form': form})


@login_required
def dashboard_view(request):

    today = timezone.localdate()

    total_products = Product.objects.count()

    total_imports = ImportRecord.objects.count()

    total_exports = ExportRecord.objects.count()

    total_projects = Project.objects.filter(owner=request.user).count()

    monthly_import_tax = ImportRecord.objects.filter(
        import_date__year=today.year,
        import_date__month=today.month,
    ).aggregate(
        total_tax=Coalesce(
            Sum('tax_amount'),
            Value(0),
            output_field=DecimalField(max_digits=12, decimal_places=2)
        )
    )['total_tax']

    monthly_export_tax = ExportRecord.objects.filter(
        export_date__year=today.year,
        export_date__month=today.month,
    ).aggregate(
        total_tax=Coalesce(
            Sum('tax_amount'),
            Value(0),
            output_field=DecimalField(max_digits=12, decimal_places=2)
        )
    )['total_tax']

    monthly_net_tax = monthly_export_tax - monthly_import_tax

    low_stock_products = Product.objects.filter(
        quantity__lt=10
    )

    display_name = request.user.get_full_name().strip() or request.user.username

    context = {

        'display_name': display_name,

        'total_products': total_products,

        'total_imports': total_imports,

        'total_exports': total_exports,

        'total_projects': total_projects,

        'monthly_import_tax': monthly_import_tax,

        'monthly_export_tax': monthly_export_tax,

        'monthly_net_tax': monthly_net_tax,

        'current_month_name': today.strftime('%B'),

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


@login_required
def submission_evidence_view(request):
    evidence_dir = Path(__file__).resolve().parent.parent / 'submission_evidence'
    image_suffixes = {'.png', '.jpg', '.jpeg', '.webp', '.gif'}

    evidence_files = []
    if evidence_dir.exists() and evidence_dir.is_dir():
        evidence_files = sorted(
            [
                item.name
                for item in evidence_dir.iterdir()
                if item.is_file() and item.suffix.lower() in image_suffixes
            ]
        )

    return render(
        request,
        'user_management/submission_evidence.html',
        {
            'evidence_files': evidence_files,
        }
    )


@login_required
def submission_evidence_file_view(request, filename):
    evidence_dir = Path(__file__).resolve().parent.parent / 'submission_evidence'
    target_file = (evidence_dir / filename).resolve()

    if not str(target_file).startswith(str(evidence_dir.resolve())):
        raise Http404('File not found.')

    if not target_file.exists() or not target_file.is_file():
        raise Http404('File not found.')

    return FileResponse(target_file.open('rb'))