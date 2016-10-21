import * as ko from 'knockout';
import * as validation from 'knockout.validation';
import * as dialog from 'plugins/dialog';
import CustomModal = require('./customModal');
import {makeMessage} from '../services/messageService';
import {MessageTypes} from '../constants/messageTypes';
import {updateRequest} from '../services/requestServices';
import {getAreas} from '../services/utils';
import {IArea} from 'areaInterfaces';
import {ICreateRequest} from 'requestInterface';

class RequestUpdateModal extends CustomModal {


    protected priority: any = ko.observable().extend({required: true, number: true, step: 1, min: 1 });
    protected target_date: any = ko.observable().extend({required: true});
    protected details: any = ko.observable().extend({required: true});
    protected product_area: any = ko.observable().extend({required: true});
    protected request_title: any = ko.observable().extend({required: true});
    private ticket_url: any = ko.observable().extend({required: true});
    protected areas: string[];
    private errors: any = validation.group(this);
    protected canSubmit: any = ko.observable(true);


    public activate() {
        this.canSubmit(true);
        this.priority(this.model.request.client_priority);
        this.target_date(this.model.request.target_date);
        this.details(this.model.request.description);
        this.product_area(this.model.request.product_area);
        this.request_title(this.model.request.title);
        this.ticket_url(this.model.request.ticket_url);
        return getAreas().then((resp: IArea[]) => {
            this.areas = resp.map((area: IArea) => {
                return area.name;
            });
        });
    }

    public submit(): void {
        this.canSubmit(false);
        if (this.errors().length > 0) {
            this.errors.showAllMessages();
        } else {
            let request: any = {
                client_priority: this.priority(),
                details: this.details(),
                product_area: this.product_area(),
                title: this.request_title(),
                target_date: this.target_date(),
                ticket_url: this.ticket_url()
            };
            updateRequest(request, this.model.request.link)
                .then((req: ICreateRequest) => {
                    makeMessage(MessageTypes.SUCCESS, 'Updated the request number ' + req.id);
                })
                .catch((err: any) => {
                    console.log('up error');
                    makeMessage(MessageTypes.DANGER, err.toString());
                });
            this.close();
        }
        this.canSubmit(true);
    }
}

export = RequestUpdateModal;
