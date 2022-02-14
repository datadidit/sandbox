import { useState } from "react";

const axios = require('axios');

const headers = {
    'Content-Type': 'application/json'
}

const AutoComplete = () => {
    const [filteredSuggestions, setFilteredSuggestions] = useState([]);
    const [activeSuggestionIndex, setActiveSuggestionIndex] = useState(0);
    const [showSuggestions, setShowSuggestions] = useState(false);
    const [input, setInput] = useState("");

    const onChange = (e) => {
        const userInput = e.target.value;

        // Filter our suggestions that don't contain the user's input
        // const unLinked = suggestions.filter(
        //     (suggestion) =>
        //         suggestion.toLowerCase().indexOf(userInput.toLowerCase()) > -1
        // );

        setInput(e.target.value);
        let search = {
            "suggest": {
                "suggestions": {
                    "prefix": e.target.value,
                    "completion": {
                        "field": "team_completion",
                        "size": 10
                    }
                }
            }
        }
        // let searchURL = "http://localhost:9200/simpson-example/_search"
        let searchURL = "http://localhost:9200/team/_search"
        axios.post(searchURL, search, {headers})
            .then((response) => {
                // console.log("Response ")
                // console.log(response)
                // console.log(Object.keys(response.data.suggest))
                let suggestions = response.data.suggest['suggestions'];
                let options = suggestions['0'].options;
                // console.log(suggestions['0'].options)
                let names = options.map(entry => {
                    let name = entry._source.name
                    console.log(name)
                    // TODO: Figure out options label
                    return name
                })
                console.log(options)
                setFilteredSuggestions(names)
            }).catch(error => {
            console.log(error)
        })
        // setFilteredSuggestions(unLinked);
        setActiveSuggestionIndex(0);
        setShowSuggestions(true);
    };

    const onClick = (e) => {
        setFilteredSuggestions([]);
        setInput(e.target.innerText);
        setActiveSuggestionIndex(0);
        setShowSuggestions(false);
    };

    const onKeyDown = (e) => {
        // User pressed the enter key
        if (e.keyCode === 13) {
            setInput(filteredSuggestions[activeSuggestionIndex]);
            setActiveSuggestionIndex(0);
            setShowSuggestions(false);
        }
        // User pressed the up arrow
        else if (e.keyCode === 38) {
            if (activeSuggestionIndex === 0) {
                return;
            }

            setActiveSuggestionIndex(activeSuggestionIndex - 1);
        }
        // User pressed the down arrow
        else if (e.keyCode === 40) {
            if (activeSuggestionIndex - 1 === filteredSuggestions.length) {
                return;
            }

            setActiveSuggestionIndex(activeSuggestionIndex + 1);
        }
    };

    const SuggestionsListComponent = () => {
        return filteredSuggestions.length ? (
            <ul className="suggestions">
                {filteredSuggestions.map((suggestion, index) => {
                    let className;

                    // Flag the active suggestion with a class
                    if (index === activeSuggestionIndex) {
                        className = "suggestion-active";
                    }

                    return (
                        <li className={className} key={suggestion} onClick={onClick}>
                            {suggestion}
                        </li>
                    );
                })}
            </ul>
        ) : (
            <div className="no-suggestions">
        <span role="img" aria-label="tear emoji">
          😪
        </span>{" "}
                <em>sorry no suggestions</em>
            </div>
        );
    };

    return (
        <>
            <input
                type="text"
                onChange={onChange}
                onKeyDown={onKeyDown}
                value={input}
            />
            {showSuggestions && input && <SuggestionsListComponent />}
        </>
    );
};

export default AutoComplete;
