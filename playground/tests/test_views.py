from django.test import TestCase, Client
from django.urls import reverse
from playground.models import Booking
from playground.forms import BookingForm
import json



class TestViews(TestCase):
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
