from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, RequestFactory
from .models import *
from decimal import Decimal
User = get_user_model()
from .views import recalc_cart, AddToCartView
user = get_user_model()


class InternetStoreCases(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Ноутбуки', slug='notebooks')
        image = SimpleUploadedFile("mb_m1.png", content=b'', content_type='image.png')
        self.notebook = Product.objects.create(
            category=self.category,
            title='TEST NOTEBOOK',
            slug='test-slug',
            image=image,
            price=Decimal('12.00'),
            description='SOME TEST TEXT',
        )
        self.customer = Customer.objects.create(
            user=self.user,
            phone='111',
            address='sdf',
        )
        self.cart = Cart.objects.create(owner=self.customer)
        self.cart_product = CartProduct.objects.create(
            user=self.customer,
            cart=self.cart,
            product=self.notebook,
        )

    def test_add_to_cart(self):
        self.cart.products.add(self.cart_product)
        recalc_cart(self.cart)
        self.assertIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(self.cart.final_price, Decimal('12.00'))

    def test_response(self):
        factory = RequestFactory()
        client = Client()
        request = factory.get('')
        response = AddToCartView.as_view()(request, slug='test-slug')
        #response = client.get('/add-to-cart/TEST NOTEBOOK/test-slug')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.url, 'base')
