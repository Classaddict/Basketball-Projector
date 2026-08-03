import { useState} from 'react'
import { Container} from 'react-bootstrap'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import { Component, NavItem,NavLink } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import Header from './Header';

export default class App extends Component {

  constructor(props){
    super(props);
    
  }

  componentDidMount(){
    document.title="Basketball Projections"
  }

  render(){  
    return(
      <Container>
          <Header />
      </Container>
  );
  }
}