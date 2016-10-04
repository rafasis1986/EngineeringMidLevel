import * as ko from 'knockout';
import * as app from 'durandal/app';
import {IRequest} from 'requestInterface';
import {createTicket} from "../services/ticketServices";
import {ITicketBase} from "ticketInterface";

class TicketRequestModel {

    protected detail: any = ko.observable();
    protected target_date: any = ko.observable();
    protected description: any = ko.observable();
    protected request_id: any = ko.observable();
    protected client_id: any = ko.observable();
    protected created_at: any = ko.observable();

    constructor (request: IRequest) {
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
                alert('creted');
            })
            .catch((err: any) => {
                console.log(err.data.detail);
                alert(err.toString());
            });
    }

    public cancel(): void {
    }


}

export = TicketRequestModel;
