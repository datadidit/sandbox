import LikeButton from "./like-button";

// This needs to be capitalized to distinguish from HTML and Javascript
const HeaderComponent = ({title}) => {
    // console.log(`Props ${title}`)
    return <h1>{title ? title : "Develop. Preview. Ship."}</h1>;
}

const ListIndex = ({name}) => {
    return <li>{name}</li>
}

const HomePage = () => {
    const names = ['Ada Lovelace', 'Grace Hopper', 'Margaret Hamilton']

    return (<div>
        {/* Nesting Header Component */}
        <HeaderComponent/>
        <ul>
            {names.map((name) => {
                // console.log(`Name ${name}`);
                return <ListIndex key={name} name={name}/>
            })}
        </ul>
        <LikeButton/>
    </div>)
};

export default HomePage;