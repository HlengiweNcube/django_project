from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_migrate)
def setup_default_groups(sender, **kwargs):
    """Create assignment role groups and map Django permissions."""
    if sender.name != 'user_management':
        return

    manager_group, _ = Group.objects.get_or_create(name='Manager')
    staff_group, _ = Group.objects.get_or_create(name='Staff')

    manager_permissions = Permission.objects.filter(
        codename__in=[
            'view_product', 'add_product', 'change_product', 'delete_product',
            'view_project', 'add_project', 'change_project', 'delete_project',
            'view_importrecord', 'add_importrecord', 'change_importrecord', 'delete_importrecord',
            'view_exportrecord', 'add_exportrecord', 'change_exportrecord', 'delete_exportrecord',
            'view_message', 'add_message', 'change_message', 'delete_message',
        ]
    )
    manager_group.permissions.set(manager_permissions)

    staff_permissions = Permission.objects.filter(
        codename__in=[
            'view_product',
            'view_project',
            'view_importrecord',
            'view_exportrecord',
            'view_message',
            'add_message',
        ]
    )
    staff_group.permissions.set(staff_permissions)


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """Ensure each user always has a profile row for contact details."""
    if created:
        UserProfile.objects.create(user=instance)
    else:
        UserProfile.objects.get_or_create(user=instance)
