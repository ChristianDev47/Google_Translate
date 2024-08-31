import { FromLanguage, Language } from '../types/types';

const API = 'https://google-translate-api-1gl9.onrender.com/api/v1/translate/';

export async function translate({
  fromLanguage,
  toLanguage,
  text,
}: {
  fromLanguage: FromLanguage;
  toLanguage: Language;
  text: string;
}) {
  if (fromLanguage === toLanguage) return text;
  try {
    const requestData = {
      text,
      fromLanguage,
      toLanguage,
    };
    const response = await fetch(API, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData),
    });
    if (response.ok) {
      const data = await response.json();
      return data.translated_text;
    }
  } catch (error) {
    console.error('Fetching Error:', error);
    throw new Error('Failed to fetch revenue data.');
  }
}
