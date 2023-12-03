from django.test import TestCase
from django.urls import reverse

def test_abaout_page_status_code(self):
    response = self.client.get(reverse("about"))
    self.assertEqual(response.status_code, 200)