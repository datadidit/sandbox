'use client'
import hljs from "highlight.js";
import {useEffect} from "react";

const CodeHighlighter = ({code, className}) => {
    useEffect(() => {
        hljs.highlightAll()
    }, [])

    return (
        <pre>
            <code className={className}>
            {`
                ${code}   
            `}
            </code>
        </pre>
    )
}

export default CodeHighlighter;