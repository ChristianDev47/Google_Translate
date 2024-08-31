# Translation API

This Translation API is a Django-based application designed to translate text between multiple languages efficiently. The API leverages Cloudflare's AI services to provide accurate translations and supports various features, including automatic language detection and customizable language options.

## Core Features

The Translation API provides the following key functionalities:

- **Text Translation**: Translate text from one language to another using Cloudflare's AI-powered translation services.
- **Language Detection**: Automatically detect the source language if it is not specified.
- **Multi-language Support**: Supports a wide range of languages for both source and target translations.
- **Error Handling**: Provides meaningful error messages when the translation fails or when the input text is not recognized as belonging to a supported language.
- **Non-Editable Result Field**: The translated text is displayed in a non-editable field, ensuring the integrity of the output.

## Additional Features

- **Auto Language Detection**: When the source language is set to 'auto', the API automatically detects the language of the input text and translates it to the specified target language.
- **Return of Original Text**: If the API cannot determine the source language, it returns the original text without modification.
- **Response Formatting**: The API ensures that the response is straightforward, providing only the translated text without additional metadata.

## Technologies Used

- **Django**: The web framework used to build the API, ensuring a robust and scalable backend.
- **Django REST Framework (DRF)**: Provides tools for building Web APIs in Django, facilitating serialization and request/response handling.
- **Cloudflare AI API**: Utilized for executing the actual translation, leveraging advanced AI models to deliver accurate translations.
- **Requests**: A Python library used for making HTTP requests to the Cloudflare API.
