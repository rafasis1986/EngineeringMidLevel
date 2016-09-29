import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import {getClients} from "../services/clientServices";
import {IClient} from "clientInterfaces";
import SimpleGrid = require("../models/simpleGrid");
import {Constant} from "../constants/enviroment";


const columns = [{ headerText: "Id", rowText: "id" },
    { headerText: "Email", rowText: "email" },
    { headerText: "Name", rowText: "full_name" },
    { headerText: "Details", rowText: "link" }];

class Clients {

    private clients: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private gridViewModel: any;


    constructor() {}

    public activate(){
        this.isLoading(true);
        return  this.loadClients().then((data) => {
                this.clients(data);
                this.gridViewModel = new SimpleGrid(this.clients, columns, Constant.PAGINATE_LIMIT);
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

    public addItem(client: IClient) {
        this.clients.push(client);
    }

    public sortByName() {
        this.clients.sort((a, b) => {
            return a.full_name < b.full_name ? -1 : 1;
        });
    }

    public sortById() {
        this.clients.sort((a, b) => {
            return a.id < b.id ? -1 : 1;
        });
    }

    public jumpToFirstPage() {
        this.gridViewModel.setCurrentPageIndex(0);
    }

    public viewDetail(clientData: IClient) {
        return app.showMessage(clientData.full_name, clientData.email);
    }
}

export = Clients;
