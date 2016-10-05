import * as ko from 'knockout';
import * as app from 'durandal/app';

import SimpleGrid = require('./simpleGrid');
import CustomDialog = require('./customModal');
import {ITicketBase} from 'ticketInterface';
import TicketDetails = require('../viewmodels/ticketDetails');


class SimpleGridTicket extends SimpleGrid {

    public showCustomModal(ticket: ITicketBase) {
        this.dialog = new CustomDialog('Ticket Details', new TicketDetails(ticket));
        this.dialog.show();
    }
}

export = SimpleGridTicket;



