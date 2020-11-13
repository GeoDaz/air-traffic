import './style.css';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom';

import HomePage from '../pages/HomePage';
import QuestionPage from '../pages/QuestionPage';
import Header from '../components/Header';

function App() {
	return (
		<div className="app">
			<Header />
			<main>
				<Router>
					<Switch>
						<Route exact path="/questions">
							<QuestionPage />
						</Route>
						<Route path="/">
							<HomePage />
						</Route>
					</Switch>
				</Router>
			</main>
		</div>
	);
}

export default App;
