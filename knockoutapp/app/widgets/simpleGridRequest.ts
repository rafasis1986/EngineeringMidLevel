import * as ko from 'knockout';
import * as app from 'durandal/app';
import SimpleGrid = require('./simpleGrid');
import CustomDialog = require('./customModal');
import {IRequest} from 'requestInterface';
import {getRequestDetails} from '../services/requestServices';
import RequestDetails = require('../viewmodels/requestDetails');
import TicketRequestModel = require('../viewmodels/ticketDetails');
import TicketModal = require('./ticketModal');


class SimpleGridRequest extends SimpleGrid {

    public showDetailModal(requestPath: any) {
        getRequestDetails(requestPath)
            .then((request: IRequest) => {
                this.dialog = new CustomDialog(request.title, new RequestDetails(request));
                this.dialog.show();
            }).catch((error: Error) => {
                console.log(error.toString());
            });
    }

    public showTicketModal(requestPath: any) {
        console.log(requestPath);
        getRequestDetails(requestPath)
            .then((request: IRequest) => {
                this.dialog = new TicketModal(request.title, new TicketRequestModel(request));
                this.dialog.show();
            }).catch((error: Error) => {
                console.log(error.toString());
            });
    }
}
export = SimpleGridRequest;



