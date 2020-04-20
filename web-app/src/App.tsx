import React, {useState} from 'react';
import {Button} from '@material-ui/core'
import './App.css';

const App: React.FC = () => {
	const [displayTitle, setTitle] = useState<string | undefined>("Default Title");

	return (
		<div className="App">
			<div className="column side">
				<Button onClick={() => setTitle("Search Title")}> Search</Button>
				<Button onClick={() => setTitle("Filter Title")}> Filter</Button>
			</div>
			<div className="column middle">
				<p>{displayTitle}</p>
			</div>
		</div>
	);
};

export default App;
