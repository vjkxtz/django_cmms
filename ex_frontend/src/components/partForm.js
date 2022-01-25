import React from 'react';
import {Button, Form, FormGroup, Input, Label} from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class partForm extends React.Component {
    state = {
        pk: 0,
        assembly: ""
    };
}