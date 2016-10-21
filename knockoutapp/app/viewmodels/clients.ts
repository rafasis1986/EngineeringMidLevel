import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import {getClients} from '../services/clientServices';
import {IClient} from 'clientInterfaces';
import SimpleGridClient = require('../widgets/simpleGridClient');
import BaseView = require('./baseView');


const columns = [{ headerText: 'Id', rowText: 'id' },
    { headerText: 'Email', rowText: 'email' },
    { headerText: 'Name', rowText: 'full_name' },
    { headerText: 'Details', rowText: 'link' }];

class Clients extends BaseView {

    private clients: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private gridViewModel: any;

    public activate(){
        this.isLoading(true);
        return  this.loadClients()
            .then((data) => {
                this.clients(data);
                this.gridViewModel = new SimpleGridClient(data, columns);
                this.isLoading(false);
                this.showMessage();
            })
            .catch((err: Error) => {
                window.location.assign('#');
            });
    }

    public loadClients(): Promise<IClient[]> {
        let deferred: Deferred<IClient[]> = Q.defer<IClient[]>();

        getClients()
            .then((clients: IClient[]) => {
                deferred.resolve(clients);
            })
            .catch((err: Error) => {
                console.log(err.toString());
                deferred.reject(err);
            });
        return deferred.promise;
    }

}

export = Clients;
