from django.test import TestCase
from django.contrib.auth.models import User

from .models import Product


# Create your tests here.
class TestViews(TestCase):

    def test_get_checkout(self):
        user = User.objects.create_superuser(username='testuser')
        user.set_password('testuser123')
        user.save()
        self.client.login(username='testuser', password='testuser123')

        product = Product.objects.create(
            name='Test product', description='Test description', price=100)

        session = self.client.session
        session['bag'] = {product.id: 1}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
