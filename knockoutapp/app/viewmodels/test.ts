

import $ = require('jquery');
import ko = require('knockout');

import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import {getClients} from '../services/clientServices';
import {IClient} from 'clientInterfaces';

import SimpleGridClient = require('../widgets/simpleGridClient');
import BaseView = require('./baseView');
import kg = require('kg');


const columns = [{ headerText: 'Id', rowText: 'id' },
    { headerText: 'Email', rowText: 'email' },
    { headerText: 'Name', rowText: 'full_name' },
    { headerText: 'Details', rowText: 'link' }];


class Tests extends BaseView {

    protected clients: any = ko.observableArray();
    protected isLoading: any = ko.observable();
    protected gridViewModel: any = ko.;
    protected myData: any = ko.observableArray([{name: "Moroni", age: 50},
                                      {name: "Tiancum", age: 43},
                                      {name: "Jacob", age: 27},
                                      {name: "Nephi", age: 29},
                                      {name: "Enos", age: 34}]);
    protected gridOptions: any = {  data: this.myData };

    public activate(){
        let jq: any = $.cssNumber;
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

export = Tests;
