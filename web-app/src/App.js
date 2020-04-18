import React from 'react';
import '@popperjs/core';
import Dropdown from "react-bootstrap/Dropdown";
import './App.css';
import DropdownButton from "react-bootstrap/DropdownButton";

function App() {
    return (
        <div className="App">
            <header className="Title-bar">
            </header>
            <body>
            <div className="panel">
                <h1>
                    Filter by:
                </h1>
                <DropdownButton id="dropdown-basic-button" title="Dropdown button">
                    <Dropdown.Item> Action One</Dropdown.Item>
                </DropdownButton>
            </div>
            <div className="panel">
                <button>

                </button>
            </div>
            </body>
        </div>
    );
}

export default App;
