from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse

from inventory.models import Product


class ImportTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username='importer',
			password='StrongPass123!@#'
		)
		add_perm = Permission.objects.get(codename='add_importrecord')
		self.user.user_permissions.add(add_perm)
		self.product = Product.objects.create(
			name='Monitor',
			category='Electronics',
			quantity=5,
			price='250.00',
			description='4K monitor'
		)

	def test_add_import_increases_stock(self):
		self.client.login(username='importer', password='StrongPass123!@#')
		response = self.client.post(
			reverse('add_import'),
			{
				'product': self.product.id,
				'supplier_name': 'Tech Supplier',
				'quantity_imported': 3,
				'import_date': '2026-05-27',
				'notes': 'Restock',
			}
		)

		self.assertEqual(response.status_code, 302)
		self.product.refresh_from_db()
		self.assertEqual(self.product.quantity, 8)
