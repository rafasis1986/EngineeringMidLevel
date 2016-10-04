import {ITicketBase} from 'ticketInterface';

class TicketDetails {

    protected ticket: ITicketBase;

    constructor (ticket: ITicketBase) {
        this.ticket = ticket;
    }
}

export = TicketDetails;
