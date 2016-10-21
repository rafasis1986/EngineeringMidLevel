import * as ko from 'knockout';
import * as validation from 'knockout.validation';
import * as app from 'durandal/app';
import {IRequest} from 'requestInterface';
import CustomModal = require('../widgets/customModal');

class TicketCreate extends CustomModal {

    protected detail: any = ko.observable().extend({required: true});
    protected target_date: any = ko.observable();
    protected description: any = ko.observable();
    protected request_id: any = ko.observable();
    protected client_id: any = ko.observable();
    protected created_at: any = ko.observable();
    private errors: any = validation.group(this);

    constructor (request: IRequest) {
        super(request.id.toString(), request);
        this.request_id(request.id);
        this.description(request.description);
        this.target_date(request.target_date);
        this.client_id(request.client_id);
        this.created_at(request.created_at);
    }

}

export = TicketCreate;
