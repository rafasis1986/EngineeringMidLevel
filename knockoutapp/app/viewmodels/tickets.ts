import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import {getTickets} from '../services/ticketServices';
import {ITicketBase} from 'ticketInterface';
import SimpleGridTicket = require('../widgets/simpleGridTicket');
import BaseView = require('./baseView');
import defer = Q.defer;


const columns = [{ headerText: 'Id', rowText: 'id' },
    { headerText: 'Request', rowText: 'request_title' },
    { headerText: 'Date', rowText: 'created_at' },
    { headerText: 'Details', rowText: 'link' }];

class Tickets extends BaseView {

    private clients: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private gridViewModel: any;


    public activate(){
        this.isLoading(true);
        this.showMessage();
        return this.loadTickets()
            .then((data) => {
                this.clients(data);
                this.gridViewModel = new SimpleGridTicket(data, columns);
                this.isLoading(false);
            })
            .catch((err: Error) => {
                console.log(err.toString());
                window.location.assign('#');
            });
    }

    public loadTickets(): Promise<ITicketBase[]> {
        let deffered: Deferred<ITicketBase[]> = Q.defer<ITicketBase[]>();
        getTickets()
            .then((tickets: ITicketBase[]) => {
                deffered.resolve(tickets);
            })
            .catch((err: Error) => {
                deffered.reject(err);
            });

        return deffered.promise;
    }

}

export = Tickets;
