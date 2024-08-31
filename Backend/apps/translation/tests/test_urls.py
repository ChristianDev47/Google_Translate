from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.translation.views import TranslateAPIView

class TestTranslationURLs(SimpleTestCase):

    def test_translate_url_resolves(self):
        url = reverse('translation:translate')
        self.assertEqual(resolve(url).func.view_class, TranslateAPIView)
