from django.urls import reverse
from django.test import TestCase
from festivals.models import Festival

class FestivalsTest(TestCase):
    
    def setUp(self):
        Festival.objects.create(user_id=1, title='test', url='test')


    def test_index(self):
        
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('slider' in response.context)
        self.assertTrue('news' in response.context)
        self.assertTrue('festivals_pl' in response.context)
        self.assertTrue('festivals_all' in response.context)
        self.assertTrue('artists' in response.context)


    def test_details(self):
        
        model = Festival.objects.get(url='test')
        # print(model.url)
        response = self.client.get(reverse('festival_details', kwargs={'url': model.url}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('festival' in response.context)
        self.assertTrue('news' in response.context)


    def test_latest_festivals(self):
        
        response = self.client.get(reverse('latest_festivals'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('festivals' in response.context)
        
        