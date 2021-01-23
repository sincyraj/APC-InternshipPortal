import React,{Component} from 'react';
import {Route,Link,BrowserRouter, Redirect} from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
class Student extends Component{
    constructor(props)
    {
        super(props);
        this.state={
            Data:[],
            isAuth:true
        }
    }
    componentWillMount()
    {
        var obj;
        fetch('http://localhost:5000/students')
        .then(response => response.json())
        .then(data => this.setState({Data:data.data}))  //obj=data)
        .then(()=>console.log(this.state.Data[0]));
        
    }
    buttonclick=(e)=>{
        const {target}=e;
        let var1=target.dataset.name;
        var data = new FormData();
        data.append('internship_id', var1);
        fetch('http://localhost:5000/students', { 
            method: 'POST',
            body:data
        });
    }
    logoutclicked=()=>{
        this.setState({isAuth:false});
    }
    render()
    {
        return(
            <div style={{backgroundColor:'red',height:'1400px'}}>
                {this.state.isAuth==false?<Redirect to="/Login"></Redirect>:
            <Container>
                <h1>Student Profile</h1>
                <Row>
                    <Col style ={{marginLeft:'50px',fontSize: 20,fontFamily: "Arial"}}><h3>TITLE</h3></Col>
                    <Col style ={{marginLeft:'70px',fontSize: 20,fontFamily: "Arial"}}><h3>Description</h3></Col>
                    <Col style ={{marginLeft:'150px',fontSize: 20,fontFamily: "Arial"}}><h3>Req Cgpa</h3></Col>
                    <Col style ={{marginLeft:'90px',fontSize: 20,fontFamily: "Arial"}}><h3>Start Date</h3></Col>
                    <Col style ={{marginLeft:'120px',fontSize: 20,fontFamily: "Arial"}}><h3>End Date</h3></Col>
                    <Col style ={{marginLeft:'50px',fontSize: 20,fontFamily: "Arial"}}><h3>Apply</h3></Col>
                </Row>
                <br/>
              {this.state.Data.map((val,i)=>(
                  <Row>
                      <Col>{val.title}</Col>
                      <Col>{val.description}</Col>
                      <Col>{val.required_cgpa}</Col>
                      <Col>{val.start_date}</Col>
                      <Col>{val.end_date}</Col>
                      <button data-name={val.id} onClick={this.buttonclick}>Apply</button>
                      <br></br>
                  </Row>
              ))}
            </Container>}
            <button onClick={this.logoutclicked}>Logout</button>
            </div>

        );
    }
}
export default Student;