import requests
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import EmailMultiAlternatives
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


class ResendEmailBackend(BaseEmailBackend):
    """Send email through Resend's HTTP API.

    This backend is useful on free hosting tiers where SMTP ports are blocked.
    """

    api_url = "https://api.resend.com/emails"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_key = getattr(settings, "RESEND_API_KEY", "")

        if not self.api_key and not self.fail_silently:
            raise ImproperlyConfigured(
                "RESEND_API_KEY is required when using ResendEmailBackend."
            )

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        sent_count = 0
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        for message in email_messages:
            try:
                payload = self._build_payload(message)
                response = requests.post(
                    self.api_url,
                    headers=headers,
                    json=payload,
                    timeout=30,
                )
                response.raise_for_status()
                sent_count += 1
            except Exception:
                if not self.fail_silently:
                    raise

        return sent_count

    def _build_payload(self, message):
        from_email = message.from_email or settings.DEFAULT_FROM_EMAIL

        payload = {
            "from": from_email,
            "to": message.to,
            "subject": message.subject,
            "text": message.body,
        }

        if isinstance(message, EmailMultiAlternatives) and message.alternatives:
            for content, mime_type in message.alternatives:
                if mime_type == "text/html":
                    payload["html"] = content
                    break

        return payload
