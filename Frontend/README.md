# Translation Frontend

A modern and intuitive frontend application built with **React** and **TypeScript**, styled using **Tailwind CSS**. This application is designed to offer a seamless and efficient text translation experience, similar to Google Translate. It includes a user-friendly interface for translating text between multiple languages with features such as language detection, translation output, and additional functionalities like text-to-speech and copying translations.

## Core Features

- **Single Tab Interface**: The application presents a clean and simple interface with a single tab, displaying the title and main components.
- **Language Selection**: Two dropdown selects allow users to choose the source and target languages for translation. One select is for detecting languages with various options, and the other is for predefined language options.
- **Language Swap**: An icon of arrows between the selects allows users to easily switch the source and target languages.
- **Text Areas for Translation**: Two text areas are provided. The first text area is where users input text to be translated, and the second text area displays the translated text.
- **Debounced Input Handling**: The application uses debouncing to manage input in the primary text area, showing a loading indicator while the translation is processed.
- **Additional Functionalities**:
  - **Copy Translation**: An icon for copying the translated text to the clipboard.
  - **Text-to-Speech**: An icon to generate and play audio of the translated text.

### Additional Features

- **Automatic Language Detection**: Supports automatic detection of the source language if it is not specified, providing a seamless translation experience.
- **Error Handling**: Displays meaningful error messages if the translation fails or the input text is not recognized.
- **Non-Editable Text Areas**: The translated text area is non-editable to ensure the integrity of the output.
- **Responsive Design**: Fully responsive layout to provide a consistent user experience across different device sizes.

## Technologies Used

- **React**: The core framework for building the frontend application.
- **TypeScript**: Adds type safety and improves code quality and maintainability.
- **Tailwind CSS**: Utility-first CSS framework used for styling and designing the application.
- **Debounce**: Technique used for managing user input and reducing the frequency of API calls during typing.
- **Text-to-Speech API**: Utilized for generating audio from the translated text.
- **Clipboard API**: Provides functionality to copy text to the clipboard.

## Overview

This frontend application is designed to offer a user-friendly and efficient translation experience. By leveraging modern technologies and best practices, the application ensures that users can easily translate text between languages, handle errors gracefully, and enjoy additional features like text-to-speech and copying translations. Whether users are translating simple phrases or complex sentences, the application provides a smooth and intuitive experience.
