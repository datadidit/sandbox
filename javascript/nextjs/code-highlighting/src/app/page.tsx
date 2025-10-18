'use client'
import CodeHighlighter from "@/app/CodeHighlighter";

// Json list of code simple hello world examples.
let codeExamples = [
    {
        "language": "html",
        "code": "<div>Hello World</div>",
        "className": "language-html"
    },
    {
        "language": "java",
        "code": "System.out.println('Hello World')",
        "className": "language-java"
    },
    {
        "language": "python",
        "code": "print('Hello World')",
        "className": "language-python"
    },
    {
        "language": "javascript",
        "code": "console.log('Hello World')",
        "className": "language-javascript"
    }
]

export default function Home() {
  return (
    <div>
        <h1 className="text-3xl font-bold underline">SYNTAX HIGHLIGHTING</h1>
        {codeExamples.map((props, idx) => {
            return (
                <div key={idx}>
                    <h2>{props.language.toUpperCase()} Example</h2>
                    <CodeHighlighter key={idx} {...props} />
                </div>
            )
        })}
    </div>
  );
}
