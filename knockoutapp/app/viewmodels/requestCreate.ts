import * as ko from 'knockout';
import * as validation from 'knockout.validation';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;

import SimpleGridRequest = require('../widgets/simpleGridRequest');
import {createRequest} from '../services/requestServices';
import BaseView = require('./baseView');
import {makeMessage} from '../services/messageService';
import {MessageTypes} from '../constants/messageTypes';
import {getClients} from "../services/clientServices";
import {IClient} from "clientInterfaces";
import {getAreas} from "../services/utils";
import {IArea} from "areaInterfaces";


class RequestCreate extends BaseView{

    private title: any = ko.observable().extend({required: true});
    private details: any = ko.observable().extend({required: true});
    private client: any = ko.observable().extend({required: true});
    private client_priority: any = ko.observable().extend({required: true, number: true, step: 1, min: 1 });
    private product_area: any = ko.observable().extend({required: true});
    private ticket_url: any = ko.observable().extend({required: true});
    private target_date: any = ko.observable().extend({required: true});
    private isLoading: any = ko.observable().extend({required: true});
    private emailClients: string[];
    private areas: string[];
    private errors: any = validation.group(this);


    public activate(){
        this.isLoading(true);
        return getClients().then((iclients: IClient[]) => {
            this.emailClients = iclients.map( (client: IClient) =>  {
                return client.email;
            });
            return getAreas();
        }).then((resp: IArea[]) => {
            this.areas = resp.map((area: IArea) => {
                return area.name;
            });
            this.isLoading(false);
        });
    }

    public submit(): void {
        let value: any;
        value = this.title() && this.details() && this.ticket_url() &&  this.target_date();.
        if (! value) {
            makeMessage(MessageTypes.WARNING, 'Please check the form');
            this.showMessage()
            this.errors.showAllMessages();
        } else {

            let request: any = {
                client: this.client(),
                client_priority: this.client_priority(),
                details: this.details(),
                product_area: this.product_area(),
                ticket_url: this.ticket_url(),
                title: this.title(),
                target_date: this.target_date()
            };
            createRequest(request)
                .then((req: any) => {
                    makeMessage(MessageTypes.SUCCESS, 'Request created');
                })
                .catch((err: any) => {
                    makeMessage(MessageTypes.DANGER, err.toString());
                });
        }
    }

}

export = RequestCreate;
