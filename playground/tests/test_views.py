from django.test import TestCase, Client
from django.urls import reverse
from playground.models import Booking
from playground.forms import BookingForm
import json



class TestViews(TestCase):
<<<<<<< HEAD

  def test_project_home_GET(self):
    client = Client()
    response = client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'index.html','base.html' )
  def test_project_about_GET(self):
    client = Client()
    response = client.get(reverse('about'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'about.html' )
  def test_project_booking_GET(self):
    client = Client()
    response = client.get(reverse('booking'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'bookings.html' )
  def test_project_cars_GET(self):
    client = Client()
    response = client.get(reverse('cars'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'cars.html' ) 
  def test_project_contact_GET(self):
    client = Client()
    response = client.get(reverse('contact'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'contacts.html' )
  def test_project_help_GET(self):
    client = Client()
    response = client.get(reverse('Help'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'help.html' )
  def test_project_category_GET(self):
    client = Client()
    response = client.get(reverse('category'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'category.html' )
  
=======
    def setUp(self):
        self.client = Client()
        self.booking_url = reverse('booking')
    def test_project_home_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html','base.html' )
    def test_booking_POST_valid(self):
        response = self.client.post(self.booking_url, {
            'client_name': 'nimsha', # replace with actual form fields
            'client_phone': ''
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm.html')
>>>>>>> target/master
