import { SectionType } from '../types/types.d';

interface Props {
  type: SectionType;
  loading?: boolean;
  onChange: (value: string) => void;
  value: string;
}

const commonStyles = { border: 0, height: '200px' };

const getPlaceholder = ({
  type,
  loading,
}: {
  type: SectionType;
  loading?: boolean;
}) => {
  if (type === SectionType.From) return 'Introducir texto';
  if (loading === true) return 'Cargando...';
  return 'Traducción';
};

export const TextArea = ({ type, loading, value, onChange }: Props) => {
  const styles =
    type === SectionType.From
      ? commonStyles
      : { ...commonStyles, backgroundColor: '#f5f5f5' };

  const handleChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    onChange(event.target.value);
  };

  return (
    <textarea
      className={`px-3 py-2 text-[18px] border-none rounded-xl focus:outline-none w-72 max-h-[200px] min-h-[200px] mb-[1.5rem] resize-none ${
        type === SectionType.From && 'bg-gray-100'
      }`}
      autoFocus={type === SectionType.From}
      disabled={type === SectionType.To}
      placeholder={getPlaceholder({ type, loading })}
      style={styles}
      value={value}
      autoCorrect="on"
      onChange={handleChange}
    />
  );
};
