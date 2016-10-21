import * as ko from 'knockout';
import * as validation from 'knockout.validation';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import SimpleGridTicket = require('../widgets/simpleGridTicket');
import BaseView = require('./baseView');
import {makeMessage} from '../services/messageService';
import {MessageTypes} from '../constants/messageTypes';
import {updateUser, confirmUpdateUser} from '../services/userServices';
import {IUser} from 'userInterfaces';


class Tickets extends BaseView {

    protected isLoading: any = ko.observable();
    protected phone: any = ko.observable().extend({required: true}).extend({ pattern: {
        message: 'This phone number doesnt match with E.164 format +582742214598',
        params: '^[+][0-9]{10,15}$'
    }});
    protected code: any = ko.observable();
    protected canSubmit: any = ko.observable(true);
    protected errors: any = validation.group(this);
    protected showConfirmation: any = ko.observable(false);

    public activate(){
        this.isLoading(true);
        this.canSubmit(true);
        this.isLoading(false);
    }

    public update(): void {
        this.canSubmit(false);
        if (this.errors().length > 0){
            this.errors.showAllMessages();
        } else {
            updateUser(this.phone()).then((resp: string) => {
                makeMessage(MessageTypes.SUCCESS, 'We sent your code confirmation ');
                this.showMessage();
                this.code.extend({required: true});
                this.phone.extend({validatable: false});
                this.displayMessage(true);
                this.showConfirmation(true);
            }).catch((err: Error) => {
                makeMessage(MessageTypes.DANGER, 'Check your phone number');
            });
        }
        this.canSubmit(true);
    }

    public confirm(): void {
        this.canSubmit(false);
        if (this.errors().length > 0){
            this.errors.showAllMessages();
        } else {
            confirmUpdateUser(this.code()).then((resp: IUser) => {
                makeMessage(MessageTypes.SUCCESS, 'We registered your new phone number ' + this.phone);
                this.showConfirmation(false);
                window.location.assign('#');
            }).catch((err: Error) => {
                makeMessage(MessageTypes.DANGER, 'check your code');
                this.showMessage();
            });
        }
        this.canSubmit(true);
    }
}

export = Tickets;
