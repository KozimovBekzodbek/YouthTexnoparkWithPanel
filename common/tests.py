from django.test import TestCase
from django.urls import reverse
app_name = 'common'
class SimpleTest(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('common:home'))
        self.assertEqual(response.status_code, 200)
