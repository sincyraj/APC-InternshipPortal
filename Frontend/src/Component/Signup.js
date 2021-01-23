import React,{Component} from 'react';
import {Route,Link,BrowserRouter, Redirect} from 'react-router-dom';

class Signup extends Component{
    constructor(props)
    {
        super(props)
        this.state={
            username:"",
            email:"",
            password:"",
            category:"",
            firstname:"",
            lastname:"",
            middlename:"",
            phno:"",
            regno:"",
            signup:false,
        }
    }
    userchanged=(e)=>{
        
        this.setState({
            username:e.target.value
        });
    }
    signupclicked=()=>
    {
        if(this.state.username==="" ||
         this.state.password==="" ||
         this.state.email==="" ||
         this.state.phno==="" ||
         this.state.regno==="" ||
         this.state.category==="" ||
         this.state.firstname==="" ||
         this.state.middlename==="" ||
         this.state.lastname==="" )
        {
            console.log("all feilds mustbe filed!");
        }
        else
        {
            var data = new FormData();
            data.append("user_name", this.state.username);
            data.append("password", this.state.password);
            data.append("email", this.state.email);
            data.append("phone_number", this.state.phno);
            data.append("registration_id", this.state.regno);
            data.append("category", this.state.category);
            data.append("first_name", this.state.firstname);
            data.append("middle_name", this.state.middlename);
            data.append("last_name", this.state.lastname);
            var bodyFormData = new FormData();
            let opts={
                'user_name':this.state.username,
                'password':this.state.password,
                'email':this.state.email,
                'phone_number':this.state.phno,
                'registration_id':this.state.regno,
                'category':this.state.category,
                'first_name':this.state.firstname,
                'middle_name':this.state.middlename,
                'last_name':this.state.lastname,
            }
            console.log(opts);
            bodyFormData.append(this.state.username,this.state.password);
            fetch('http://localhost:5000/register', { 
                method: 'POST',
                body:data
            });
            this.setState({signup:true});

        }
    }
    passwordchanged=(e)=>{
            this.setState({password:e.target.value});
    }
    phnochanged=(e)=>{
        this.setState({phno:e.target.value});
    }
    emailchanged=(e)=>{
        this.setState({email:e.target.value});
    }
    fnamechanged=(e)=>{
        this.setState({firstname:e.target.value});
    }
    mnamechanged=(e)=>{
        this.setState({middlename:e.target.value});
    }
    lnamechanged=(e)=>{
        this.setState({lastname:e.target.value});
    }
    regchanged=(e)=>{
        this.setState({regno:e.target.value});
    }
    studentclick=(e)=>{
        this.setState({category:"student"});
    }
    uniclick=(e)=>{
        this.setState({category:"university"});
    }
    companyclick=(e)=>{
        this.setState({category:"company"});
    }
    render(){
        return (
            
            <div>
                {this.state.signup==true?<Redirect to ="/Login"></Redirect>:
                <div>
                <h1>SignUp Portal</h1>
                <div>
                    <input type="text"
                    placeholder="username"
                    onChange={this.userchanged}
                    />
                    <br></br>
                    <input type="text"
                    placeholder="email"
                    onChange={this.emailchanged}
                    />
                    <br></br>
                    <input type="text"
                    placeholder="firstname"
                    onChange={this.fnamechanged}
                    />
                    <br></br>
                    <input type="text"
                    placeholder="middlename"
                    onChange={this.mnamechanged}
                    />
                    <br></br>
                    <input type="text"
                    placeholder="last name"
                    onChange={this.lnamechanged}
                    />
                    <br></br>
                    <input type="text"
                    placeholder="registration number"
                    onChange={this.regchanged}
                    />
                    <br></br>
                    <input type="text"
                    placeholder="phone number"
                    onChange={this.phnochanged}
                    />
                    <br></br>
                    <input type="text"
                    placeholder="password"
                    onChange={this.passwordchanged}
                    />
                    <br></br>
                    <label>Select category</label>
                    <button onClick={this.studentclick}>Student</button>
                    <button onClick={this.companyclick}>Company</button>
                    <button onClick={this.uniclick}>University</button>
                    <br></br>
                    <button
                        onClick={this.signupclicked}
                    >signup</button>
                </div>
            </div>}
            </div>
        );
    }
}
export default Signup;
