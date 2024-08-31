from django.test import TestCase
from apps.translation.serializers import TranslationRequestSerializer

class TranslationRequestSerializerTestCase(TestCase):

    def test_translation_request_serializer_valid_data(self):
        """Test serializer with valid data."""
        data = {
            'text': 'Hello, how are you?',
            'toLanguage': 'es',
            'fromLanguage': 'en'
        }
        serializer = TranslationRequestSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, data)

    def test_translation_request_serializer_valid_data_default_fromLanguage(self):
        """Test serializer with valid data and default fromLanguage."""
        data = {
            'text': 'Hello, how are you?',
            'toLanguage': 'es'
        }
        serializer = TranslationRequestSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['fromLanguage'], 'auto')
        self.assertEqual(serializer.validated_data['text'], 'Hello, how are you?')
        self.assertEqual(serializer.validated_data['toLanguage'], 'es')

    def test_translation_request_serializer_missing_text(self):
        """Test serializer with missing text field."""
        data = {
            'toLanguage': 'es',
            'fromLanguage': 'en'
        }
        serializer = TranslationRequestSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('text', serializer.errors)

    def test_translation_request_serializer_invalid_toLanguage(self):
        """Test serializer with invalid toLanguage (exceeds max_length)."""
        data = {
            'text': 'Hello, how are you?',
            'toLanguage': 'es1234567890',  
            'fromLanguage': 'en'
        }
        serializer = TranslationRequestSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('toLanguage', serializer.errors)

    def test_translation_request_serializer_empty_text(self):
        """Test serializer with empty text field."""
        data = {
            'text': '',
            'toLanguage': 'es',
            'fromLanguage': 'en'
        }
        serializer = TranslationRequestSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('text', serializer.errors)

    def test_translation_request_serializer_empty_toLanguage(self):
        """Test serializer with empty toLanguage field."""
        data = {
            'text': 'Hello, how are you?',
            'toLanguage': '',
            'fromLanguage': 'en'
        }
        serializer = TranslationRequestSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('toLanguage', serializer.errors)
