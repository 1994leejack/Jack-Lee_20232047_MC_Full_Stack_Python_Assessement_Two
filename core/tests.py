from django.test import TestCase
from django.urls import reverse
from .models import RenewablePowerGeneration, Article, Subscriber
from core.views import energy_data


class ModelsTestCase(TestCase):
    def setUp(self):
        RenewablePowerGeneration.objects.create(mode_of_generation='Solar', contribution_twh=10.5)
        Article.objects.create(title='Test Article', content='Test Content')

    def test_renewable_power_generation_model(self):
        solar_generation = RenewablePowerGeneration.objects.get(mode_of_generation='Solar')
        self.assertEqual(solar_generation.contribution_twh, 10.5)

    def test_article_model(self):
        test_article = Article.objects.get(title='Test Article')
        self.assertEqual(test_article.content, 'Test Content')


class ViewsTestCase(TestCase):
    def setUp(self):
        RenewablePowerGeneration.objects.create(mode_of_generation='Biofuel', contribution_twh=777.65)
        RenewablePowerGeneration.objects.create(mode_of_generation='Wind', contribution_twh=8.2)

    def test_energy_data_view(self):
        response = self.client.get(reverse('energy_data'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['data'], RenewablePowerGeneration.objects.all(), ordered=False)    

    def test_subscribe_view(self):
        response = self.client.get(reverse('subscribe'))
        self.assertEqual(response.status_code, 200)


class SubscriberModelTestCase(TestCase):
    def setUp(self):
        self.existing_email = 'existing@example.com'
        Subscriber.objects.create(email=self.existing_email)

    def test_subscribe_existing_email(self):
        response = self.client.post(reverse('subscribe'), {'email': self.existing_email})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'subscribe_error.html')


    def test_subscribe_success(self):
        email = 'new@example.com'
        response = self.client.post(reverse('subscribe'), {'email': email})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('subscribe_success'))

class EnergyDataTestCase(TestCase):
    def test_energy_data_sort_highest_to_lowest(self):
        response = self.client.get(reverse('energy_data') + '?sort_order=highest_to_lowest')
        self.assertEqual(response.status_code, 200)
        
    