from django.test import TestCase
from django.contrib.auth.models import User

from .models import Product


# Create your tests here.
class TestViews(TestCase):

    def test_get_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail(self):
        product = Product.objects.create(
            name='Test product', description='Test description', price=100)
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_get_add_product(self):
        user = User.objects.create_superuser(username='testuser')
        user.set_password('testuser123')
        user.save()
        self.client.login(username='testuser', password='testuser123')

        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_get_edit_product(self):
        user = User.objects.create_superuser(username='testuser')
        user.set_password('testuser123')
        user.save()
        self.client.login(username='testuser', password='testuser123')

        product = Product.objects.create(
            name='Test product', description='Test description', price=100)

        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
