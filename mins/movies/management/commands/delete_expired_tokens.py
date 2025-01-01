from django.core.management.base import BaseCommand
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from django.utils import timezone

class Command(BaseCommand):
  help = 'Deletes all expired tokens and flushes tokens from the blacklist'

  def handle(self, *args, **kwargs):
    now = timezone.now()

    # Delete expired outstanding tokens
    expired_outstanding_tokens = OutstandingToken.objects.filter(expires_at__lt=now)
    expired_outstanding_count = expired_outstanding_tokens.count()
    expired_outstanding_tokens.delete()

    # Delete corresponding blacklisted tokens
    expired_blacklisted_tokens = BlacklistedToken.objects.filter(token__expires_at__lt=now)
    expired_blacklisted_count = expired_blacklisted_tokens.count()
    expired_blacklisted_tokens.delete()

    self.stdout.write(self.style.SUCCESS(f'Successfully deleted {expired_outstanding_count} expired outstanding tokens'))
    self.stdout.write(self.style.SUCCESS(f'Successfully deleted {expired_blacklisted_count} expired blacklisted tokens'))
