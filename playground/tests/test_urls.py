from django.test import SimpleTestCase
from django.urls import reverse, resolve
from playground.views import home


class TestUrls(SimpleTestCase):

    def test_home_joy_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)