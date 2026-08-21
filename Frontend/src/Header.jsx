import {Component} from "react";
import {Card, CardTitle, CardBody, CardText } from "react-bootstrap"
import './Header.css';
export default class header extends Component{
    
    render(){
        return(
            <Card className="card">
                <CardTitle className="d-flex align-items-center justify-content-center gap-3 mb-0">
                    <img src="Images/openclipart-vectors-basketball-147794.svg" alt="Basketball JPEG" style={{width:"200px", height:"100px"}} />
                    <h1 className="mb-0">Basketball Projections</h1>
                    <img src="Images/openclipart-vectors-basketball-147794.svg" alt="Basketball JPEG" style={{width:"200px", height:"100px"}} />
                </CardTitle>
                <CardBody>
                    <h4><i>Projecting your favorite players stats!</i></h4>
                </CardBody>
            </Card>
        );
    }
}