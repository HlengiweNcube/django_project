from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from datetime import date
from pathlib import Path

from .models import UserProfile
from inventory.models import Product
from imports.models import ImportRecord
from exports.models import ExportRecord


class UserManagementTests(TestCase):
	def test_registration_creates_user_and_assigns_staff_group(self):
		response = self.client.post(
			reverse('register'),
			{
				'username': 'newuser',
				'email': 'newuser@example.com',
				'password1': 'StrongPass123!@#',
				'password2': 'StrongPass123!@#',
			}
		)

		self.assertRedirects(response, reverse('dashboard'))
		user = User.objects.get(username='newuser')
		self.assertTrue(user.groups.filter(name='Staff').exists())
		self.assertTrue(UserProfile.objects.filter(user=user).exists())

	def test_dashboard_requires_login(self):
		response = self.client.get(reverse('dashboard'))
		self.assertEqual(response.status_code, 302)

	def test_password_reset_page_available(self):
		response = self.client.get(reverse('password_reset'))
		self.assertEqual(response.status_code, 200)

	def test_update_profile_saves_contact_details(self):
		user = User.objects.create_user(
			username='profileuser',
			email='profile@example.com',
			password='StrongPass123!@#'
		)
		self.client.login(username='profileuser', password='StrongPass123!@#')
		response = self.client.post(
			reverse('update_profile'),
			{
				'username': 'profileuser',
				'email': 'updated@example.com',
				'first_name': 'Jane',
				'last_name': 'Doe',
				'phone_number': '55512345',
				'address': '1 Main Street',
				'city': 'Auckland',
				'country': 'NZ',
				'postal_code': '1010',
			}
		)

		self.assertEqual(response.status_code, 302)
		user.refresh_from_db()
		self.assertEqual(user.email, 'updated@example.com')
		self.assertEqual(user.profile.city, 'Auckland')

	def test_dashboard_shows_current_month_tax_totals(self):
		user = User.objects.create_user(
			username='taxuser',
			email='tax@example.com',
			password='StrongPass123!@#'
		)
		self.client.login(username='taxuser', password='StrongPass123!@#')

		product = Product.objects.create(
			name='Tax Product',
			category='Electronics',
			quantity=50,
			price='100.00',
			description='Test product for tax totals'
		)

		ImportRecord.objects.create(
			product=product,
			supplier_name='Supplier A',
			quantity_imported=2,
			import_date=date.today(),
			notes='Test import',
		)

		ExportRecord.objects.create(
			product=product,
			customer_name='Customer A',
			quantity_exported=3,
			export_date=date.today(),
			notes='Test export',
		)

		response = self.client.get(reverse('dashboard'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['monthly_import_tax'], 30)
		self.assertEqual(response.context['monthly_export_tax'], 45)
		self.assertEqual(response.context['monthly_net_tax'], 15)

	def test_submission_evidence_page_requires_login(self):
		response = self.client.get(reverse('submission_evidence'))
		self.assertEqual(response.status_code, 302)

	def test_submission_evidence_page_displays_for_authenticated_user(self):
		user = User.objects.create_user(
			username='evidenceuser',
			email='evidence@example.com',
			password='StrongPass123!@#'
		)
		self.client.login(username='evidenceuser', password='StrongPass123!@#')

		response = self.client.get(reverse('submission_evidence'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'user_management/submission_evidence.html')

	def test_submission_evidence_file_serves_existing_image(self):
		user = User.objects.create_user(
			username='fileuser',
			email='fileuser@example.com',
			password='StrongPass123!@#'
		)
		self.client.login(username='fileuser', password='StrongPass123!@#')

		evidence_path = Path(__file__).resolve().parent.parent / 'submission_evidence'
		filename = '01_tests_all_ok.png'
		if not (evidence_path / filename).exists():
			self.skipTest('Expected submission evidence image not found in repository.')

		response = self.client.get(reverse('submission_evidence_file', args=[filename]))
		self.assertEqual(response.status_code, 200)
