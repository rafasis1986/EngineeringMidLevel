import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import {IRequest} from 'requestInterface';
import SimpleGridRequest = require('../widgets/simpleGridRequest');
import {getRequests} from '../services/requestServices';
import {IRequestBase} from 'requestInterface';
import BaseView = require('./baseView');
import * as userSession from "../singletons/userSession";
import {Constant} from "../constants/enviroment";


const columns = [{ headerText: 'Id', rowText: 'id' },
    { headerText: 'Title', rowText: 'title' },
    { headerText: 'Client', rowText: 'client_id' },
    { headerText: 'Priority', rowText: 'client_priority' },
    { headerText: 'Area', rowText: 'product_area' },
    { headerText: 'Target Date', rowText: 'target_date' },
    { headerText: 'Attended', rowText: 'attended' },
    { headerText: 'Details', rowText: 'link' },
];

class Requests extends BaseView {

    private requests: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private gridViewModel: any;
    private isClient: any = ko.observable(false);

    public activate() {
        this.isLoading(true);
        if (userSession.getUserRoles().search(Constant.ROLE_CLIENT) != -1) {
            this.isClient(true);
        }
        return  this.loadRequests().then((data) => {
                this.requests(data);
                this.gridViewModel = new SimpleGridRequest(data, columns);
                this.isLoading(false);
        });
    }

    public loadRequests(): JQueryDeferred<IRequestBase[]> {
        return system.defer((dfd) => {
            setTimeout( () => {
                getRequests().then((requests: IRequest[]) => {
                    dfd.resolve(requests); })
                    .catch((err: Error) => {
                        console.log(err.toString());
                        window.location.assign('#');
                    });
            }, 500);
        });
    }
}

export = Requests;
