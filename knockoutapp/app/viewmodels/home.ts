import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import {IHomeMessage} from 'homeInterfaces';
import {getMeInfo} from '../services/userServices';
import {IUser} from 'userInterfaces';
import {setApiUrls} from '../services/urlServices';
import {Constant} from '../constants/enviroment';
import BaseView = require('./baseView');
import {getUserFullName, getUserEmail} from "../singletons/userSession";


class Home extends BaseView {

    private messages: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private email: any = ko.observable();
    private full_name: any = ko.observable();

    public activate() {
        this.isLoading(true);
        this.full_name(getUserFullName());
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