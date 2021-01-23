import React,{Component} from 'react';
import Signup from './Signup.js';
import {Redirect} from 'react-router-dom';
class Login extends Component{
    constructor(props)
    {
        super(props)
        this.state={
            username:"",
            password:"",
            signup:false,
            Data:{},
            LoggedIn:false,
            category:""
        }
    }
    userchanged=(e)=>{
        
        this.setState({
            username:e.target.value
        });
        console.log(this.state.username);
    }
    loginclicked=()=>
    {
        if(this.state.username==="" || this.state.password==="" )
        {
            console.log("all feilds mustbe filed!");
        }
        else
        {
            var bodyFormData = new FormData();
            var data = new FormData();
            data.append("username", this.state.username);
            data.append("password", this.state.password);
            bodyFormData.append(this.state.username,this.state.password);
            fetch('http://localhost:5000/login', { 
                method: 'POST',
                body:data
            }).then(response => response.json())
            .then((data)=>this.setState({Data:data}));
            console.log(this.state.Data.status);
            if(this.state.Data.category=="student")
            {
                this.setState({LoggedIn:true,category:"student"})
            }
            else if(this.state.Data.category=="company")
            {
                this.setState({LoggedIn:true,category:"company"})
            }
            else if(this.state.Data.category=="university")
            {
                this.setState({LoggedIn:true,category:"university"})
            }
            /*fetch('http://localhost:5000/login')
            .then(response => response.json())
            .catch((err) => {
                // Do something for an error here
                console.log("Error Reading data "+err)});*/
        }
    }
    passwordchanged=(e)=>{
            this.setState({password:e.target.value});
            console.log(this.state.password);
    }
    labelclicked=()=>{
        this.setState({signup:true});
    }
    render(){
        return (
            <div>{
                this.state.LoggedIn==true && this.state.category=="student"?<Redirect to="/Student"></Redirect>:
                this.state.LoggedIn==true && this.state.category=="company"?<Redirect to="/Company"></Redirect>:
                this.state.LoggedIn==true && this.state.category=="university"?<Redirect to="/University"></Redirect>:
            <div>
                {this.state.signup==true?<Redirect to="/Signup"></Redirect>
                :<div>
                <h1>Login Portal</h1>
                <div>
                    <input type="text"
                    placeholder="username"
                    onChange={this.userchanged}
                    />
                    <br></br>
                    <input type="text"
                    placeholder="password"
                    onChange={this.passwordchanged}
                    />
                    <br></br>
                    <br></br>
                    <label onClick={this.labelclicked}>
                        Not a member?SignUp.
                    </label>
                    <br></br>
                    <button
                        onClick={this.loginclicked}
                    >Login</button>

                </div>
    </div>}
            </div>}
            </div>
        );
    }
}
export default Login;
