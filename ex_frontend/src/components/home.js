import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import PartList from "./partList";
import partModal from "./partmodal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    part: []
  };

  componentDidMount() {
    this.resetState();
  }

  getpart = () => {
    axios.get(API_URL).then(res => this.setState({ part: res.data }));
  };

  resetState = () => {
    this.getpart();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <PartList
              part={this.state.part}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <partModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;