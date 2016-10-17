import * as ko from 'knockout';
import * as validation from 'knockout.validation';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import {getTickets} from '../services/ticketServices';
import {ITicketBase} from 'ticketInterface';
import SimpleGridTicket = require('../widgets/simpleGridTicket');
import BaseView = require('./baseView');
import {makeMessage} from "../services/messageService";
import {MessageTypes} from "../constants/messageTypes";
import {updateUser, confirmUpdateUser} from "../services/userServices";
import {IUser} from "userInterfaces";


class Tickets extends BaseView {

    protected isLoading: any = ko.observable();
    protected phone: any = ko.observable().extend({required: true});
    protected code: any = ko.observable().extend({required: true});
    protected errors: any = validation.group(this);
    protected showConfirmation: any = ko.observable(false);

    public activate(){
        this.isLoading(true);
        this.isLoading(false);
    }

    public update(): void {
        if (! this.phone()){
            makeMessage(MessageTypes.WARNING, 'Please check the form');
            this.showMessage();
            this.errors.showAllMessages();
        } else {
            updateUser(this.phone()).then((resp: string) => {
                makeMessage(MessageTypes.SUCCESS, 'We sent your code confirmation ');
                this.showConfirmation(true);
            }).catch((err: Error) => {
                makeMessage(MessageTypes.DANGER, err.toString());
            });
            this.showMessage();
        }
    }

    public confirm(): void {
        if (! this.phone()){
            makeMessage(MessageTypes.WARNING, 'Please check the form');
            this.showMessage();
            this.errors.showAllMessages();
        } else {
            confirmUpdateUser(this.code()).then((resp: IUser) => {
                makeMessage(MessageTypes.SUCCESS, 'We registered your new phone number ' + resp.phone_number);
                this.showConfirmation(false);
                window.location.assign('#');
            }).catch((err: Error) => {
                console.log(err);
                console.log('err');
                makeMessage(MessageTypes.DANGER, err.toString());
            });
        }
    }
}

export = Tickets;
