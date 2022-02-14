import logo from './logo.svg';
import React from 'react';
import './App.css';
import Autocomplete from "./autocomplete/Autocomplete";
import "./style.css";
import TextField from '@mui/material/TextField';
// import Autocomplete from '@mui/material/Autocomplete';
// TODO: Why is this not an import
const axios = require('axios');

const headers = {
    'Content-Type': 'application/json'
}

function App(){
    return (
        <div className="wrapper">
            <h1>React Autocomplete</h1>
            <h2>Want to see something cool?, start typing</h2>
            <Autocomplete
                suggestions={[
                    "Angular",
                    "Blitzjs",
                    "Gatsby",
                    "Reactjs",
                    "Vuejs",
                    "Svelte",
                    "Nextjs",
                    "Node",
                    "Express",
                    "Sails",
                    "Loopback",
                    "React-router",
                    "Redux",
                    "Flux",
                    "Yarn",
                    "Npm"
                ]}
            />
        </div>
    );
}

/*function App(){
  const [value, setValue] = React.useState(null);
  const [inputValue, setInputValue] = React.useState('');
  const [options, setOptions] = React.useState([])

  return (
      <div className="App">
        <header className="App-header">
          <div>{`value: ${value !== null ? `'${value}'` : 'null'}`}</div>
          <div>{`inputValue: '${inputValue}'`}</div>
          <br />
          <Autocomplete
              value={value}
              onChange={(event, newValue) => {
                // console.log("on change called")
                setValue(newValue);
              }}
              inputValue={inputValue}
              onInputChange={(event, newInputValue) => {
                // console.log("on input change called")
                setInputValue(newInputValue);
                // Original Simpson Suggestor
                // let search = {
                //     "suggest": {
                //         "simpson-suggest": {
                //             "prefix": newInputValue,
                //             "completion": {
                //                 "field": "name_completion"
                //             }
                //         }
                //     }
                // }
                let search = {
                    "suggest": {
                        "suggestions": {
                            "prefix": newInputValue,
                            "completion": {
                                "field": "team_completion"
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
                        setOptions(names)
                    }).catch(error => {
                        console.log(error)
                    })
              }}
              id="controllable-states-demo"
              options={options}
              sx={{ width: 300 }}
              renderInput={(params) => <TextField {...params} label="Controllable" />}
          />
        </header>
      </div>
  )
}*/
/*function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}*/



export default App;
