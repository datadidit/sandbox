'use client'
import {useEffect} from "react";

import hljs from "highlight.js";
// This throws error said highlightjs not detected.
// import 'highlightjs-line-numbers.js'

const CodeHighlighter = ({code, className, includeLineNumbers=false}) => {
    useEffect(() => {
        hljs.highlightAll()
    }, [])

    // if(includeLineNumbers) {
    //     useEffect(() => {
    //         hljs.initLineNumbersOnLoad()
    //     }, [])
    // }

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