import { useEffect } from 'react';
import { LanguageSelector } from './components/LanguageSelector';
import { TextArea } from './components/TextArea';
import { AUTO_LANGUAGE, VOICE_FOR_LANGUAGE } from './constants/constants';
import { useStore } from './hooks/useStore';
import './index.css';
import { translate } from './services/translate';
import { SectionType } from './types/types.d';
import { useDebounce } from './hooks/useDebounce';
import { ClipboardIcon, SpeakerIcon } from './components/Icons';

function App() {
  const {
    loading,
    fromLanguage,
    toLanguage,
    fromText,
    result,
    setFromLanguage,
    setToLanguage,
    interchangeLanguages,
    setFromText,
    setResult,
  } = useStore();
  const debouncedFromText = useDebounce(fromText, 300);

  useEffect(() => {
    if (debouncedFromText === '') return;

    translate({ fromLanguage, toLanguage, text: debouncedFromText })
      .then((result) => {
        if (result == null) return;
        setResult(result);
      })
      .catch(() => {
        setResult('Error');
      });
  }, [debouncedFromText, fromLanguage, toLanguage]);

  const handleClipboard = () => {
    navigator.clipboard.writeText(result).catch(() => {});
  };

  const handleSpeak = () => {
    const utterance = new SpeechSynthesisUtterance(result);
    utterance.lang = VOICE_FOR_LANGUAGE[toLanguage];
    utterance.rate = 0.9;
    speechSynthesis.speak(utterance);
  };

  return (
    <>
      <div className="flex flex-col items-center justify-center h-screen min-w-[750px] min-h-[335px] p-[3rem]">
        <h1 className="mt-5 text-4xl font-semibold">Google Translate</h1>
        <div className="grid grid-cols-7 mt-8 ">
          <div className="col-span-3 row-span-1">
            <LanguageSelector
              onChange={setFromLanguage}
              type={SectionType.From}
              value={fromLanguage}
            />
          </div>
          <div className="flex justify-center col-span-1 row-span-1 bg-transparent rounded-md">
            <button
              disabled={fromLanguage === AUTO_LANGUAGE}
              onClick={interchangeLanguages}
            >
              <svg
                focusable="false"
                width="24"
                height="24"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
              >
                <path d="M6.99 11L3 15l3.99 4v-3H14v-2H6.99v-3zM21 9l-3.99-4v3H10v2h7.01v3L21 9z"></path>
              </svg>
            </button>
          </div>
          <div className="col-span-3 row-span-1">
            <LanguageSelector
              onChange={setToLanguage}
              type={SectionType.To}
              value={toLanguage}
            />
          </div>
          <div className="col-span-3 row-span-1 bg-gray-100 rounded-md min-w-[290px] my-2">
            <TextArea
              type={SectionType.From}
              value={fromText}
              onChange={setFromText}
            />
          </div>
          <div className="col-span-1 row-span-1"></div>
          <div className="relative col-span-3 row-span-1 my-2 overflow-hidden bg-gray-100 rounded-md">
            <TextArea
              loading={loading}
              type={SectionType.To}
              value={result}
              onChange={setResult}
            />
            <div className="absolute flex gap-2 bottom-2 right-3">
              <button onClick={handleClipboard}>
                <ClipboardIcon />
              </button>
              <button onClick={handleSpeak}>
                <SpeakerIcon />
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
