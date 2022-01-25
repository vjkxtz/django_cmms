import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import partForm from "./partForm";

class partModal extends Component {
    state = {
        modal: false,
    };

    toggle = () => {
        this.setState(previous => ({
            modal: !previous.modal
        }));
    };

    render() {
        const create = this.props.create;

        var title = "cmms"
        var button = <Button onClick={this.toggle}>Edit</Button>;
        if (create) {
            title = "creating entry";

            button = (
                <button class="btn btn-primary" className= "float-right" onClick={this.toggle}>Create</button>
            );
        };

        return (
            <Fragment>
                {button}
                <Modal isOpen={this.state.modal} toggle={this.toggle}>
                    <ModalHeader toggle={this.toggle}>{title}</ModalHeader>
                    <ModalBody>
                        <partForm
                            resetState={this.props.resetState}
                            toggle={this.toggle}
                            assembly={this.props.assembly}
                        />
                    </ModalBody>
                </Modal>
            </Fragment>
        );
    };
}

export default partForm;