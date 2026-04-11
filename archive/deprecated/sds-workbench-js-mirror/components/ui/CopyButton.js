import { jsx as _jsx } from "react/jsx-runtime";
import { useState } from 'react';
import { copyToClipboard } from '../../utils/export';
export function CopyButton({ text, label = 'Copy', className = 'btn btn-sm' }) {
    const [copied, setCopied] = useState(false);
    const handle = async () => {
        await copyToClipboard(text);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };
    return (_jsx("button", { className: className, onClick: handle, children: copied ? '✓ Copied' : label }));
}
