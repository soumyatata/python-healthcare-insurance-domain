import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        {/* Other Routes for quote, login, etc. */}
      </Switch>
    </Router>
  );
}

export default App;
