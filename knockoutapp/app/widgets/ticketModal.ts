import * as dialog from 'plugins/dialog';
import CustomModal = require('./customModal');
import {createTicket} from '../services/ticketServices';
import {ITicketBase} from 'ticketInterface';
import {makeMessage} from '../services/messageService';
import {MessageTypes} from '../constants/messageTypes';

class TicketModal extends CustomModal {

    public success(): void {
        let value: any;
        value = this.model.detail() ;
        if (! value){
            makeMessage(MessageTypes.WARNING, 'Please check the form');
            this.model.errors.showAllMessages();
        } else {
            let ticket: any = {
                request_id: this.model.request_id(),
                detail: this.model.detail()
            };
            createTicket(ticket)
                .then((t: ITicketBase) => {
                    makeMessage(MessageTypes.SUCCESS, 'Ticket created number: ' + t.id);
                })
                .catch((err: any) => {
                    makeMessage(MessageTypes.DANGER, err.toString());
                });
            this.close();
        }
    }
}

export = TicketModal;
