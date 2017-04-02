from django.urls import reverse
from django.test import TestCase

class FestivalsTest(TestCase):

    def test_latest_news(self):
        
        response = self.client.get(reverse('latest_news'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('news' in response.context)

        
        