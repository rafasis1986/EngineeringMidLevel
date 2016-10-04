import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import {getTickets} from '../services/ticketServices';
import {ITicketBase} from 'ticketInterface';
import SimpleGridTicket = require('../widgets/simpleGridTicket');


const columns = [{ headerText: 'Id', rowText: 'id' },
    { headerText: 'Request', rowText: 'request_title' },
    { headerText: 'Date', rowText: 'created_at' },
    { headerText: 'Details', rowText: 'link' }];

class Tickets {

    private clients: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private gridViewModel: any;

    constructor() {}

    public activate(){
        this.isLoading(true);
        return  this.loadTickets().then((data) => {
                this.clients(data);
                this.gridViewModel = new SimpleGridTicket(data, columns);
                this.isLoading(false);
        });
    }

    public loadTickets(): JQueryDeferred<ITicketBase[]> {
        return system.defer((dfd) => {
            setTimeout( () => {
                getTickets().then((tickets: ITicketBase[]) => {
                    dfd.resolve(tickets); })
                    .catch((err: Error) => {
                        console.log(err.toString());
                        window.location.assign('#');
                    });
            }, 500);
        });
    }

}

export = Tickets;
