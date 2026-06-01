from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse

from .models import Product, Project


class InventoryTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username='staffmember',
			password='StrongPass123!@#'
		)
		self.manager = User.objects.create_user(
			username='manager',
			password='StrongPass123!@#'
		)
		add_perm = Permission.objects.get(
			codename='add_product',
			content_type__app_label='inventory'
		)
		self.manager.user_permissions.add(add_perm)

	def test_product_list_requires_login(self):
		response = self.client.get(reverse('product_list'))
		self.assertEqual(response.status_code, 302)

	def test_user_without_permission_cannot_add_product(self):
		self.client.login(username='staffmember', password='StrongPass123!@#')
		response = self.client.post(
			reverse('add_product'),
			{
				'name': 'Laptop',
				'category': 'Electronics',
				'quantity': 10,
				'price': '1999.99',
				'description': 'Test product',
			}
		)
		self.assertEqual(response.status_code, 403)

	def test_user_with_permission_can_add_product(self):
		self.client.login(username='manager', password='StrongPass123!@#')
		response = self.client.post(
			reverse('add_product'),
			{
				'name': 'Laptop',
				'category': 'Electronics',
				'quantity': 10,
				'price': '1999.99',
				'description': 'Test product',
			}
		)
		self.assertEqual(response.status_code, 302)
		self.assertTrue(Product.objects.filter(name='Laptop').exists())

	def test_user_without_project_permission_cannot_add_project(self):
		self.client.login(username='staffmember', password='StrongPass123!@#')
		response = self.client.post(
			reverse('add_project_item'),
			{
				'name': 'Site Upgrade',
				'description': 'Upgrade website infrastructure',
				'start_date': '2026-06-01',
				'end_date': '2026-06-10',
				'stakeholders': 'IT, Operations',
				'status': 'planned',
				'category': 'technology',
			}
		)
		self.assertEqual(response.status_code, 403)

	def test_user_with_project_permission_can_add_project(self):
		project_perm = Permission.objects.get(
			codename='add_project',
			content_type__app_label='inventory'
		)
		self.manager.user_permissions.add(project_perm)
		self.client.login(username='manager', password='StrongPass123!@#')
		response = self.client.post(
			reverse('add_project_item'),
			{
				'name': 'Site Upgrade',
				'description': 'Upgrade website infrastructure',
				'start_date': '2026-06-01',
				'end_date': '2026-06-10',
				'stakeholders': 'IT, Operations',
				'status': 'planned',
				'category': 'technology',
			}
		)
		self.assertEqual(response.status_code, 302)
		self.assertTrue(Project.objects.filter(name='Site Upgrade').exists())
