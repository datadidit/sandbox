'use client'
import hljs from "highlight.js";
import { useEffect } from "react";

export default function Home() {
    useEffect(() => {
        hljs.highlightAll()
    }, [])
  return (
    <div>
        <h1 className="text-3xl font-bold underline">SYNTAX HIGHLIGHTING</h1>
        <div>
            <h2>HTML Example</h2>
            <pre>
                <code className="html">
                    {`
                    <div>Hello World</div>
                    `}
                </code>
            </pre>
        </div>
        <div>
            <h2>Java Example</h2>
            <pre>
                <code className="language-java">
                    {`
                    System.out.println("Hello World")
                    `}
                </code>
            </pre>
        </div>
        <div>
            <h2>Python Example</h2>
            <pre>
                <code className="language-python">
                    {`
                     print("Hello World")
                    `}
                </code>
            </pre>
        </div>
        <div>
            <h2>Javascript Example</h2>
            <pre>
                <code className="language-javascript">
                    {`
                     console.log("Hello World");
                    `}
                </code>
            </pre>
        </div>
    </div>
  );
}
