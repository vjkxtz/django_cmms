import React from 'react';
import {Button, Form, FormGroup, Input, Label} from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class partForm extends React.Component {
    state = {
        pk: 0,
        assembly: ""
    };

    componentDidMount() {
        if (this.props.assembly) {
            const {pk, assembly} = this.props.assembly;
            this.setState({pk, assembly});
        }
    };

    onChange = e => {
        this.setState({[e.target.assembly]: e.target.value});
    };

    createPart = e => {
        e.preventDefault();
        axios.post(API_URL, this.state).then(() => {
            this.props.resetstate();
            this.props.toggle();
        });
    };

    editPart = e => {
        e.preventDefault();
        axios.put(API_URL,this.state.pk, this.state).then(() => {
            this.props.resetstate();
            this.props.toggle();
        });
    };

    defaultIfEmpty = value => {
        return value === ""?"" : value;
    };

    render(){
        return (
            <Form onSubmit={this.props.part ? this.editPart : this.createPart }>
                <FormGroup>
                    <Label for="assembly">Assembly:</Label>
                    <Input type="text" name="assembly" onChange={this.onChange} value={this.defaultIfEmpty(this.state.assembly)}/>
                </FormGroup>
                <Button>Send</Button>
            </Form>
            
        );
    }
}

export default partForm ;