from django.test import TestCase, Client
from django.urls import reverse

from .models import Stock
from accounts.models import Account

# Create your tests here.
class StockModelTests(TestCase):
    def test_ticker_label(self):
        stock = Stock(ticker='AAPL')
        field_label = stock._meta.get_field('ticker').verbose_name
        self.assertEquals(field_label, 'ticker')

    def test_stock_data_label(self):
        stock = Stock()
        field_label = stock._meta.get_field('stock_data').verbose_name
        self.assertEquals(field_label, 'stock data')

    def test_str_representation(self):
        stock = Stock(ticker='AAPL')
        self.assertEqual(str(stock), stock.ticker)
        
    # def test_file_upload(self):
    #     stock = Stock(ticker='AAPL')
    #     with open('path/to/file.csv', 'w') as f:
    #         stock.stock_data.save('file.csv', f)
    #         self.assertEqual(stock.stock_data.name, 'stocks/file.csv')

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_dashboard(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_documentation(self):
        response = self.client.get(reverse('documentation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'documentation.html')
        
    def test_add_credits(self):
        response = self.client.post(reverse('add_credits'))
        self.assertEqual(response.status_code, 401) #if the user is not authenticated
    
class AddCreditsViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.account = Account(email="testuser@gmail.com")
        self.account.set_password('12345')
        self.account.is_active = True
        self.account.save()

    def test_add_credits(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.post(reverse('add_credits'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["credits"], 10)
        
    def test_add_credits_not_authenticated(self):
        response = self.client.post(reverse('add_credits'))
        self.assertEqual(response.status_code, 401)