import React, { Component} from 'react';
import {Table} from "reactstrap";
import partmodal from "./partmodal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class PartList extends Component {
    render() {
        const part = this.props.part;
        return (
            <Table dark>
                <thead>
                    <tr>
                        <th>Assembly</th>
                    </tr>
                </thead>
                <tbody>
                    {!part || part.length <= 0 ? (
                        <tr>
                            <td colspan="1" align="center">
                                <b>Ops, no one here yet</b>
                            </td>
                        </tr>
                    ):(
                        part.map(part => (
                            <tr key={part.pk}>
                                <td>{part.assembly}</td>
                                <td align="center">
                                    <partModal create={false} part={part} resetState = {this.props.resetState}/>
                                    &nbsp; &nbsp;
                                    <ConfirmRemovalModal
                                    pk = {part.pk}
                                    resetState={this.props.resetState}/>
                                </td>
                            </tr>
                        ))
                    )}
                </tbody>
            </Table>
        )
    }
}

export default PartList;