from django.test import TestCase,Client
from .models import Publisher

class TestGreetingView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_greeting_view(self):
        response = self.client.get('/test/greeting')
        self.assertEquals(response.status_code, 200)
class TestPublisherModel(TestCase):
    def setUp(self):
        self.p = Publisher(name = "Packt", website = "www.packt.com",
                           email= "contact@packt.com")

    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)

    def test_str_representation(self):
        self.assertEquals(str(self.p), "Packt")

# Create your tests here.