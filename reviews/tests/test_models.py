from django.test import TestCase
from reviews.models import Book, Publisher, Contributor

class TestPublisherModel(TestCase):
    def test_publisher_model(self):
        publisher = Publisher.objects.create(name = "Test_Publisher_name", website = "www.test.com", email = "test@emeil.com")
        self.assertIsInstance(publisher, Publisher)