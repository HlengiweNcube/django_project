from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse

from inventory.models import Product


class ExportTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username='exporter',
			password='StrongPass123!@#'
		)
		add_perm = Permission.objects.get(codename='add_exportrecord')
		self.user.user_permissions.add(add_perm)
		self.product = Product.objects.create(
			name='Desk',
			category='Furniture',
			quantity=12,
			price='199.99',
			description='Office desk'
		)

	def test_add_export_decreases_stock(self):
		self.client.login(username='exporter', password='StrongPass123!@#')
		response = self.client.post(
			reverse('add_export'),
			{
				'product': self.product.id,
				'customer_name': 'ABC Corp',
				'quantity_exported': 4,
				'export_date': '2026-05-27',
				'notes': 'Customer shipment',
			}
		)

		self.assertEqual(response.status_code, 302)
		self.product.refresh_from_db()
		self.assertEqual(self.product.quantity, 8)

	def test_export_cannot_exceed_available_stock(self):
		self.client.login(username='exporter', password='StrongPass123!@#')
		response = self.client.post(
			reverse('add_export'),
			{
				'product': self.product.id,
				'customer_name': 'ABC Corp',
				'quantity_exported': 99,
				'export_date': '2026-05-27',
				'notes': 'Invalid shipment',
			}
		)

		self.assertEqual(response.status_code, 200)
		self.product.refresh_from_db()
		self.assertEqual(self.product.quantity, 12)
