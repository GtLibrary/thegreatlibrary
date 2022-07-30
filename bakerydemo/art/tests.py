from django.test import TestCase

# Create your tests here.

from django.test import override_settings
from django_dramatiq.test import DramatiqTestCase


class ArtTestCase(DramatiqTestCase):

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_add(self):
        print('test_add')

