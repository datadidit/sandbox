const SuggestionsListComponent = () => {
    return filteredSuggestions.length ? (
        <ul class="suggestions">
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
        <div class="no-suggestions">
            <em>No suggestions, you're on your own!</em>
        </div>
    );
};