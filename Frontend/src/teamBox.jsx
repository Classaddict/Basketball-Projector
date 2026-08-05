import { Component } from "react";
import {
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  Container
} from 'reactstrap';

export default class TeamBox extends Component{
    state={dropOpen:false, setDrop:false}

    toggle=()=>{
        this.setState((prevState)=>({dropOpen:!prevState.dropOpen}));
    }

    render(){
        const{dropOpen}=this.state;
        return(
            <Container>
                <Dropdown isOpen={dropOpen} toggle={this.toggle}>
                    <DropdownToggle>Select Team</DropdownToggle>
                    <DropdownMenu>
                        <DropdownItem header>Teams</DropdownItem>
                        <DropdownItem>Test</DropdownItem>
                    </DropdownMenu>
                </Dropdown>
            </Container>
        );
    }
}