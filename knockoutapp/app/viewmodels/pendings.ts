import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import {IRequest} from 'requestInterface';
import SimpleGridRequest = require('../widgets/simpleGridRequest');
import {getPendingRequests, getRequestDetails, updateRequestPriorityList} from '../services/requestServices';
import {IRequestBase} from 'requestInterface';
import BaseView = require('./baseView');
import * as userSession from '../singletons/userSession';
import {Constant} from '../constants/enviroment';
import RequestDetails = require('./requestDetails');
import CustomModal = require('../widgets/customModal');
import {makeMessage} from '../services/messageService';
import {MessageTypes} from '../constants/messageTypes';

const columns = [{ headerText: 'Id', rowText: 'id' },
    { headerText: 'Title', rowText: 'title' },
    { headerText: 'Client', rowText: 'client_id' },
    { headerText: 'Priority', rowText: 'client_priority' },
    { headerText: 'Area', rowText: 'product_area' },
    { headerText: 'Target Date', rowText: 'target_date' },
    { headerText: 'Attended', rowText: 'attended' },
    { headerText: 'Details', rowText: 'link' },
];

class Pendings extends BaseView {

    private pendingsLegacy: any = ko.observableArray();
    private pendings: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private isClient: any = ko.observable(false);
    private dialog: any = null;
    private canSubmit: any = ko.observable(false);

    public activate() {
        this.isLoading(true);
        if (userSession.getUserRoles().search(Constant.ROLE_CLIENT) != -1) {
            this.isClient(true);
        }
        return  this.loadPendings()
            .then((data) => {
                this.pendingsLegacy(data);
                this.pendings(data);
                this.isLoading(false);
                this.canSubmit(true);
            })
            .catch((err: Error) => {
                window.location.assign('#');
            });
    }

    public loadPendings(): Promise<IRequestBase[]> {
        let deferred: Deferred<IRequestBase[]> = Q.defer<IRequestBase[]>();

        getPendingRequests()
            .then((requests: IRequestBase[]) => {
                deferred.resolve(requests);
            })
            .catch((err: Error) => {
                deferred.reject(err);
            });

        return deferred.promise;
    }

    public showDetailModal(requestPath: any) {
        getRequestDetails(requestPath)
            .then((request: IRequest) => {
                this.dialog = new CustomModal(request.title, new RequestDetails(request));
                this.dialog.show();
            }).catch((error: Error) => {
                console.log(error.toString());
            });
    }

    public reset() {
        this.activate();
    }

    public  submit() {
        this.canSubmit(false);
        let orderIds: number[];
        orderIds = this.pendings().map((request: IRequestBase) => {
           return request.id;
        });
        updateRequestPriorityList(orderIds)
            .then((resp:any) => {
                makeMessage(MessageTypes.SUCCESS, 'Updated Priority List');
                this.showMessage();
                this.activate();
            }).catch((error: Error) => {
                makeMessage(MessageTypes.WARNING, 'We have a trouble updating the list');
                this.showMessage();
            });
        this.canSubmit(true);
    }
}

export = Pendings;
