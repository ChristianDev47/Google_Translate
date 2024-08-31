from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TranslationRequestSerializer
from .services import translate_text 

class TranslateAPIView(APIView):
    def post(self, request):
        serializer = TranslationRequestSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            toLanguage = serializer.validated_data['toLanguage']
            fromLanguage = serializer.validated_data['fromLanguage']

            translated_text = translate_text(text, toLanguage, fromLanguage)
            return Response({"translated_text": translated_text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
