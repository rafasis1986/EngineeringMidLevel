import * as ko from 'knockout';
import * as app from 'durandal/app';
import * as dialog from 'plugins/dialog';
import {IRequest} from 'requestInterface';
import {createTicket} from '../services/ticketServices';
import {ITicketBase} from 'ticketInterface';
import {makeMessage} from '../services/messageService';
import {MessageTypes} from '../constants/messageTypes';
import CustomModal = require('../widgets/customModal');

class TicketCreate extends CustomModal {

    protected detail: any = ko.observable();
    protected target_date: any = ko.observable();
    protected description: any = ko.observable();
    protected request_id: any = ko.observable();
    protected client_id: any = ko.observable();
    protected created_at: any = ko.observable();

    constructor (request: IRequest) {
        super(request.id.toString(), request);
        this.request_id(request.id);
        this.description(request.description);
        this.target_date(request.target_date);
        this.client_id(request.client_id);
        this.created_at(request.created_at);
    }

    public success(): void {
        let ticket: any = {
            request_id: this.request_id(),
            detail: this.detail()
        };
        createTicket(ticket)
            .then((t: ITicketBase) => {
                makeMessage(MessageTypes.SUCCESS, 'Ticket created');
                alert('success');
            })
            .catch((err: any) => {
                makeMessage(MessageTypes.DANGER, err.toString());

            });

    }

    public cancel(): void {
        dialog.close(this);
    }

}

export = TicketCreate;
