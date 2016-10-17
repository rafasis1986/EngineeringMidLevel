import * as dialog from 'plugins/dialog';
import CustomModal = require('./customModal');
import {createTicket} from '../services/ticketServices';
import {ITicketBase} from 'ticketInterface';
import {makeMessage} from '../services/messageService';
import {MessageTypes} from '../constants/messageTypes';
import {deleteRequest} from "../services/requestServices";

class RequestDeleteModal extends CustomModal {

    public success(): void {
        deleteRequest(this.model.request.link).then((resp: boolean) => {
            makeMessage(MessageTypes.INFO, 'Deleted request number: ' + this.model.request.id);
        }).catch((err: any) => {
            makeMessage(MessageTypes.DANGER, err.toString());
        });
        this.close();
    }
}

export = RequestDeleteModal;
