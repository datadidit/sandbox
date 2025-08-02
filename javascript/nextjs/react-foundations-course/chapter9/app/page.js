import { useState } from 'react';

// This needs to be capitalized to distinguish from HTML and Javascript
const HeaderComponent = ({title}) => {
    // console.log(`Props ${title}`)
    return <h1>{title ? title : "Develop. Preview. Ship."}</h1>;
}

const ListIndex = ({name}) => {
    return <li>{name}</li>
}

export default HomePage = () => {
    const names = ['Ada Lovelace', 'Grace Hopper', 'Margaret Hamilton']

    const [likes, setLikes] = useState(0);

    const handleClick = () => {
        setLikes(likes + 1);
    }

    return (<div>
        {/* Nesting Header Component */}
        <HeaderComponent/>
        <ul>
            {names.map((name) => {
                // console.log(`Name ${name}`);
                return <ListIndex key={name} name={name}/>
            })}
        </ul>
        <button onClick={handleClick}>Like({likes})</button>
    </div>)
};