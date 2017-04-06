from django.urls import reverse
from django.test import TestCase
from festivals.models import Festival, Artist

class FestivalsTest(TestCase):
    
    def setUp(self):
        Festival.objects.create(user_id=1, title='test', url='test')
        Artist.objects.create(title='test', url='test', status=1)


    def test_index(self):
        
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('slider' in response.context)
        self.assertTrue('news' in response.context)
        self.assertTrue('festivals_pl' in response.context)
        self.assertTrue('festivals_all' in response.context)
        self.assertTrue('artists' in response.context)


    def test_festival_details(self):
        
        model = Festival.objects.get(url='test')
        response = self.client.get(reverse('festival_details', kwargs={'url': model.url}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('festival' in response.context)
        self.assertTrue('news' in response.context)


    def test_latest_festivals(self):
        
        response = self.client.get(reverse('latest_festivals'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('festivals' in response.context)

    
    def test_artists_list(self):
            
        response = self.client.get(reverse('artists_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('artists' in response.context)
    

    def test_artist_details(self):
            
        model = Artist.objects.get(url='test')
        response = self.client.get(reverse('artist_details', kwargs={'url': model.url}))
        self.assertEqual(response.status_code, 200)

        
        