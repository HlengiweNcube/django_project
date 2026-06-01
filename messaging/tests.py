from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Message


class MessagingTests(TestCase):
	def setUp(self):
		self.sender = User.objects.create_user(
			username='sender',
			password='StrongPass123!@#'
		)
		self.receiver = User.objects.create_user(
			username='receiver',
			password='StrongPass123!@#'
		)
		self.other_user = User.objects.create_user(
			username='other',
			password='StrongPass123!@#'
		)
		self.message = Message.objects.create(
			sender=self.sender,
			receiver=self.receiver,
			subject='Hello',
			content='Important update'
		)

	def test_only_receiver_can_archive_message(self):
		self.client.login(username='other', password='StrongPass123!@#')
		response = self.client.get(reverse('archive_message', args=[self.message.id]))
		self.assertEqual(response.status_code, 404)

		self.client.login(username='receiver', password='StrongPass123!@#')
		response = self.client.get(reverse('archive_message', args=[self.message.id]))
		self.assertEqual(response.status_code, 302)
		self.message.refresh_from_db()
		self.assertTrue(self.message.is_archived)
