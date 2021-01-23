import logo from './logo.svg';
import './App.css';
import Login from './Component/Login.js';
import Signup from './Component/Signup.js'
import Student from './Component/student.js';
import Company from './Component/company.js';
import University from './Component/university.js';
import {BrowserRouter as Router,Route,Link,NavLink,Switch} from 'react-router-dom';
function App() {
  return (
    
      
    <Router>
    <div className="App">
      <Login/>
      <Switch><Route exact path="/Signup" component={Signup}></Route></Switch>
      <Switch><Route exact path="/Login" component={Login}></Route></Switch>
      <Switch><Route exact path="/Student" component={Student}></Route></Switch>
      <Switch><Route exact path="/Company" component={Company}></Route></Switch>
      <Switch><Route exact path="/University" component={University}></Route></Switch>

    </div>
    
    </Router>
    
  );
}

export default App;
