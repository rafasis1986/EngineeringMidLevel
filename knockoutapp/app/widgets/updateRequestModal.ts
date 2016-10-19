import * as ko from 'knockout';
import * as dialog from 'plugins/dialog';
import CustomModal = require('./customModal');
import {createTicket} from '../services/ticketServices';
import {ITicketBase} from 'ticketInterface';
import {makeMessage} from '../services/messageService';
import {MessageTypes} from '../constants/messageTypes';
import {deleteRequest} from "../services/requestServices";
import {getAreas} from "../services/utils";
import {IArea} from "areaInterfaces";

class UpdateRequestModal extends CustomModal {

    protected priority: any = ko.observable();
    protected target_date: any = ko.observable();
    protected details: any = ko.observable();
    protected product_area: any = ko.observable();
    protected request_title: any = ko.observable();
    protected areas: string[];


    public activate() {
        this.priority(this.model.request.client_priority);
        this.target_date(this.model.request.target_date);
        this.details(this.model.request.description);
        this.product_area(this.model.request.product_area);
        this.request_title(this.model.request.title);
        return getAreas().then((resp: IArea[]) => {
            this.areas = resp.map((area: IArea) => {
                return area.name;
            });
        });
    }

}

export = UpdateRequestModal;
