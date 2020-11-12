import logo from "./logo.svg";
import "./App.css";
import { Switch, Route, BrowserRouter as Router } from "react-router-dom";

import Table from "./components/Table";
import HomePage from "./pages/HomePage";
import QuestionPage from "./pages/QuestionPage";

function App() {
    return (
        <div className="App">
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <a class="navbar-brand" href="/">
                    Aeroport
                </a>
                <button
                    class="navbar-toggler"
                    type="button"
                    data-toggle="collapse"
                    data-target="#navbarNav"
                    aria-controls="navbarNav"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item active">
                            <a class="nav-link" href="/questions">
                                Questions <span class="sr-only">(current)</span>
                            </a>
                        </li>
                    </ul>
                </div>
            </nav>
            <main className="container">
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
