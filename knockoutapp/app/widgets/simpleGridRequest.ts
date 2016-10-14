import * as ko from 'knockout';
import * as app from 'durandal/app';
import SimpleGrid = require('./simpleGrid');
import CustomDialog = require('./customModal');
import {IRequest} from 'requestInterface';
import {getRequestDetails} from '../services/requestServices';
import RequestDetails = require('../viewmodels/requestDetails');
import TicketRequestModel = require('../viewmodels/ticketCreate');
import TicketModal = require('./ticketModal');
import {navigate} from 'plugins/history';
import {Constant} from "../constants/enviroment";
import {UserSingleton} from "../singletons/userSingleton";


class SimpleGridRequest extends SimpleGrid {

    protected isEmployee: any = ko.observable(false);

    constructor (data: any[], colums?: any[], pageSize?: number) {
        super(data, colums, pageSize);

        if (UserSingleton.getRoles().search(Constant.ROLE_EMPLOYEE) != -1) {
            this.isEmployee(true);
        }
    }


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
        getRequestDetails(requestPath)
            .then((request: IRequest) => {
                this.dialog = new TicketModal(request.title, new TicketRequestModel(request));
                this.dialog.show().then((resp:any) =>{
                    navigate('#tickets');
                });
            }).catch((error: Error) => {
                console.log(error.toString());
            });
    }
}
export = SimpleGridRequest;



