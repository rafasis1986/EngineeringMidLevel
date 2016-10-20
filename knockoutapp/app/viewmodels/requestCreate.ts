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
import {getAreas} from '../services/utils';
import {IArea} from 'areaInterfaces';
import {navigate} from 'plugins/history';
import * as userSession from '../singletons/userSession';


class RequestCreate extends BaseView{

    private title: any = ko.observable().extend({required: true});
    private details: any = ko.observable().extend({required: true});
    private client: any = ko.observable();
    private client_priority: any = ko.observable().extend({required: true, number: true, step: 1, min: 1 });
    private product_area: any = ko.observable().extend({required: true});
    private ticket_url: any = ko.observable().extend({required: true}).extend({ pattern: {
        message: 'This url doesnt match with a format like http://asdf.com',
        params: '^http://[a-zA-Z0-9]{1,30}.[a-zA-Z0-9]{2,5}$'
    }});
    private target_date: any = ko.observable().extend({required: true});
    private isLoading: any = ko.observable().extend({required: true});
    private areas: string[];
    private errors: any = validation.group(this);


    public activate(){
        this.isLoading(true);
        this.client(userSession.getUserEmail());
        return getAreas().then((resp: IArea[]) => {
            this.areas = resp.map((area: IArea) => {
                return area.name;
            });
            this.isLoading(false);
        });
    }

    public submit(): void {
        let value: any;
        value = this.title() && this.details() && this.ticket_url() &&  this.target_date();
        if (! value){
            makeMessage(MessageTypes.WARNING, 'Please check the form');
            this.showMessage();
            this.errors.showAllMessages();
        } else {

            let request: any = {
                client: userSession.getUserEmail(),
                client_priority: this.client_priority(),
                details: this.details(),
                product_area: this.product_area(),
                ticket_url: this.ticket_url(),
                title: this.title(),
                target_date: this.target_date()
            };
            createRequest(request)
                .then((req: any) => {
                    makeMessage(MessageTypes.SUCCESS, 'Created the request number ' + req.id);
                    navigate('#requests');
                })
                .catch((err: any) => {
                    makeMessage(MessageTypes.DANGER, err.toString());
                });
        }
    }

}

export = RequestCreate;
