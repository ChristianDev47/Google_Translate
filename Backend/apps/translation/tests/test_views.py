from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch

class TranslateAPIViewTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('translation:translate')
        self.valid_data = {
            'text': 'Hello, world!',
            'toLanguage': 'es',
            'fromLanguage': 'en'
        }
        self.invalid_data = {
            'text': '',
            'toLanguage': 'es'
        }

    @patch('apps.translation.views.translate_text')
    def test_translate_api_view_success(self, mock_translate_text):
        mock_translate_text.return_value = '¡Hola, mundo!'
        
        response = self.client.post(self.url, self.valid_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('translated_text', response.data)
        self.assertEqual(response.data['translated_text'], '¡Hola, mundo!')
        mock_translate_text.assert_called_once_with('Hello, world!', 'es', 'en')

    def test_translate_api_view_invalid_data(self):
        response = self.client.post(self.url, self.invalid_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('text', response.data)

    def test_translate_api_view_missing_from_language(self):
        data = {
            'text': 'Hello, world!',
            'toLanguage': 'es'
        }
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.assertIn('translated_text', response.data)

    @patch('apps.translation.views.translate_text')
    def test_translate_api_view_custom_from_language(self, mock_translate_text):
        mock_translate_text.return_value = '¡Hola, mundo!'
        
        data = {
            'text': 'Hello, world!',
            'toLanguage': 'es',
            'fromLanguage': 'fr'  
        }
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['translated_text'], '¡Hola, mundo!')
        mock_translate_text.assert_called_once_with('Hello, world!', 'es', 'fr')
