import React,{Component} from 'react';
import {Redirect} from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
class Company extends Component{
    constructor(props)
    {
        super(props);
        this.state={
            Data:[],
            Internship_code:"",
            Title:"",
            Description:"",
            Required_Gpa:"",
            endDate:"",
            isAuth:true
        }
    }
    logoutclicked=()=>{
        this.setState({isAuth:false});
    }
    onInternship_code=(e)=>{
        this.setState({Internship_code:e.target.value})
    }
    onTitle=(e)=>{
        this.setState({Title:e.target.value})
    }
    onDescription=(e)=>{
        this.setState({Description:e.target.value})
    }
    onRequired_Gpa=(e)=>{
        this.setState({Required_Gpa:e.target.value})
    }
    onendDate=(e)=>{
        this.setState({endDate:e.target.value})
    }
    componentWillMount()
    {
        var obj;
        fetch('http://localhost:5000/companies')
        .then(response => response.json())
        .then(data => this.setState({Data:data.data}))  //obj=data)
        .then(()=>console.log(this.state.Data));
        
    }
    buttonclick=(e)=>{
        var data = new FormData();
        data.append('title', this.state.Title);
        data.append('description', this.state.Description);
        data.append('required_gpa', this.state.Required_Gpa);
        data.append('internship_code', this.state.Internship_code);
        data.append('comments', this.state.endDate);
        

        fetch('http://localhost:5000/companies', { 
            method: 'POST',
            body:data
        });
    }
    render()
    {
        return(
               
            <div style={{backgroundColor:'red',height:'1400px'}}>
                {this.state.isAuth==false?<Redirect to="/Login"></Redirect>:null}
            <Container>
            <h1>Company Profile</h1>
            <Row>
                    <Col style ={{marginLeft:'220px',fontSize: 20,fontFamily: "Arial"}}><h3>Name</h3></Col>
                    <Col style ={{marginLeft:'50px',fontSize: 20,fontFamily: "Arial"}}><h3>Int. code</h3></Col>
                    <Col style ={{marginLeft:'50px',fontSize: 20,fontFamily: "Arial"}}><h3>Title</h3></Col>
                    <Col style ={{marginLeft:'30px',fontSize: 20,fontFamily: "Arial"}}><h3>Discription</h3></Col>
                    <Col style ={{marginLeft:'60px',fontSize: 20,fontFamily: "Arial"}}><h3>Req Cgpa</h3></Col>
                    
                </Row>
                  {this.state.Data.map((val,i)=>(
                  <Row>
                      <Col >{val.id}</Col>
                      <Col >{val.student}</Col>
                      <Col >{val.internship_code}</Col>
                      <Col >{val.title}</Col>
                      <Col >{val.description}</Col>
                      <Col >{val.required_cgpa}</Col>
                      
                  </Row>
              ))}
            </Container>
            <h1>Add internships</h1>
            <div>
                <input onChange={this.onInternship_code} placeholder="Internship code" type="text"></input>
                <input onChange={this.onTitle} placeholder="Title" type="text"></input>
                <input onChange={this.onDescription} placeholder="Description" type="text"></input>
                <input onChange={this.onRequired_Gpa} placeholder="Required Gpa" type="text"></input>
                <input onChange={this.onendDate} placeholder="endDate" type="text"></input>
                <br></br>
                <button onClick={this.buttonclick}>Enter</button>
            </div>
            <button onClick={this.logoutclicked}>Logout</button>
            </div>
        );
    }
}
export default Company;