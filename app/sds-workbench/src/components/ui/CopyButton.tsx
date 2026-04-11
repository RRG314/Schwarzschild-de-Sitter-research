import { useState } from 'react';
import { copyToClipboard } from '../../utils/export';

export function CopyButton({ text, label = 'Copy', className = 'btn btn-sm' }: { text: string; label?: string; className?: string }) {
  const [copied, setCopied] = useState(false);
  const handle = async () => {
    await copyToClipboard(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };
  return (
    <button className={className} onClick={handle}>
      {copied ? '✓ Copied' : label}
    </button>
  );
}
