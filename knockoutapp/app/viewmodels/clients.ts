import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import {getClients} from '../services/clientServices';
import {IClient} from 'clientInterfaces';
import SimpleGridClient = require('./simpleGridClient');


const columns = [{ headerText: 'Id', rowText: 'id' },
    { headerText: 'Email', rowText: 'email' },
    { headerText: 'Name', rowText: 'full_name' },
    { headerText: 'Details', rowText: 'link' }];

class Clients {

    private clients: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private gridViewModel: any;

    constructor() {}

    public activate(){
        this.isLoading(true);
        return  this.loadClients().then((data) => {
                this.clients(data);
                this.gridViewModel = new SimpleGridClient(data, columns);
                this.isLoading(false);
        });
    }

    public loadClients(): JQueryDeferred<IClient[]> {
        return system.defer((dfd) => {
            setTimeout( () => {
                getClients().then((clients: IClient[]) => {
                    dfd.resolve(clients); })
                    .catch((err: Error) => {
                        console.log(err.toString());
                        window.location.assign('#');
                    });
            }, 500);
        });
    }

}

export = Clients;
