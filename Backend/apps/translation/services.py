import requests
from django.conf import settings

url = settings.API_BASE_URL
headers = {"Authorization": f"Bearer {settings.API_AUTH_TOKEN}"}

def translate_text(text, target_language, source_language='auto'):
    model = "@cf/meta/llama-3-8b-instruct"
    inputs = [
        { "role": "system", "content": "You are a translator that translates text between languages. Only provide the translation of the text, without additional explanations or context." },
        { "role": "user", "content": f"Translate the following text from {source_language} to {target_language}: {text}" }
    ]
    
    response = requests.post(f"{url}{model}", headers=headers, json={"messages": inputs})
    
    if response.status_code == 200:
        result = response.json()
        translated_text = result.get('result', {}).get('response', 'Translation failed')

        # Attempt to extract only the translated sentence(s)
        start = translated_text.find('\"') + 1
        end = translated_text.rfind('\"')
        if start != -1 and end != -1 and start < end:
            translated_text = translated_text[start:end]

        # If the translation failed or the result is the same as the input, return the original text.
        if translated_text == text or 'Translation failed' in translated_text:
            return text

        return translated_text.strip()
    else:
        return f"Error: {response.status_code} - {response.text}"