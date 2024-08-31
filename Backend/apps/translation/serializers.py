from rest_framework import serializers

class TranslationRequestSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000)
    toLanguage = serializers.CharField(max_length=10)
    fromLanguage = serializers.CharField(max_length=10, required=False, default='auto')
