import React,{Component} from 'react';
import {Redirect} from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
class University extends Component{
    constructor(props)
    {
        super(props);
        this.state={
            Data:[],
            decision:"",
            isAuth:true
        }
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
        fetch('http://localhost:5000/internships')
        .then(response => response.json())
        .then(data => this.setState({Data:data.data}))  //obj=data)
        .then(()=>console.log(this.state.Data));
        
    }
    rejectclick=(e)=>{
        const {target}=e;
        let var1=target.dataset.name;
        this.setState({decision:"reject"})
        console.log(this.state.decision);
        var data = new FormData();
        data.append('id', var1);
        data.append('decision', this.state.decision);
    
        fetch('http://localhost:5000/internships', { 
            method: 'POST',
            body:data
        });
    }
    approveclick=(e)=>{
        const {target}=e;
        let var1=target.dataset.name;
        this.setState({decision:"approve"})
        console.log(this.state.decision);
        var data = new FormData();
        data.append('id', var1);
        data.append('decision', this.state.decision);
    
        fetch('http://localhost:5000/internships', { 
            method: 'POST',
            body:data
        });
    }
    logoutclicked=()=>{
        this.setState({isAuth:false});
    }
    render()
    {
        const body ={
            backgroundColor: '#282c34',
            color: 'white',
            padding: '40px',
            fontFamily: 'Arial',
            textAlign: 'center',
          }
          const body2 ={
            backgroundColor: '#282c34',
            color: 'white',
            
            padding: '40px',
            fontFamily: 'Arial',
            textAlign: 'center',
          }  
        return(
            <div style={{backgroundColor:'red',height:'1400px'}}>
                {this.state.isAuth==false?<Redirect to="/Login"></Redirect>:
            <Container>
                <h1 >University Profile</h1>
                <Row>
                    <Col style ={{width:'20%',fontSize: 20,fontFamily: "Arial"}}><h3>First Name</h3></Col>
                    <Col style ={{width:'20%',fontSize: 20,fontFamily: "Arial"}}><h3>Last Name</h3></Col>
                    <Col style ={{width:'20%',fontSize: 20,fontFamily: "Arial"}}><h3>Req Cgpa</h3></Col>
                    <Col style ={{width:'20%',fontSize: 20,fontFamily: "Arial"}}><h3>Title</h3></Col>
                    <Col style ={{width:'20%',fontSize: 20,fontFamily: "Arial"}}><h3>Description</h3></Col>
                    <Col style ={{width:'20%',fontSize: 20,fontFamily: "Arial"}}><h3>Gpa</h3></Col>
                    
                </Row>
                <Container>
                  {this.state.Data.map((val,i)=>(
                  <Row >
                      <Col style={{width:'20%'}}>{val.first_name}</Col>
                      <Col style={{width:'25%'}}>{val.last_name}</Col>
                      <Col style={{width:'50%'}}>{val.required_gpa}</Col>
                      <Col style={{width:'20%'}}>{val.title}</Col>
                      <Col style={{width:'20%'}}>{val.description}</Col>
                      <Col style={{width:'20%'}}>{val.student_cgpa}</Col>
                      <button data-name={val.internship_id} onClick={this.rejectclick}>Reject</button>
                      <button data-name={val.internship_id} onClick={this.approveclick}>Accept</button>

                  </Row>
                  
              ))}
              <button onClick={this.logoutclicked}>Logout</button>
            </Container>
            </Container>}
            </div>
        );
    }
}
export default University;