import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import {IHomeMessage} from 'homeInterfaces';
import BaseView = require('./baseView');
import {getUserFullName, getUserEmail, getUserPicture} from '../singletons/userSession';


class Home extends BaseView {

    private messages: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private email: any = ko.observable();
    private fullName: any = ko.observable();
    private profilePicture: any = ko.observable();

    public activate() {
        this.isLoading(true);
        this.fullName(getUserFullName());
        if (getUserPicture() != 'null') {
            this.profilePicture(getUserPicture());
        }
        this.messages(this.loadMessages());
        this.email(getUserEmail());
        this.isLoading(false);
    }

    public loadMessages(): IHomeMessage[] {
        return [{
                title: 'Welcome to IWS-TEST',
                content: 'Use the navbar menu to move to other options'
        }];
    }
}


export = Home;