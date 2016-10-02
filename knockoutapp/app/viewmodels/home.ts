import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import {IMessage} from 'homeInterfaces';
import {getMeInfo} from '../services/userServices';
import {IUser} from 'userInterfaces';
import {setApiUrls} from '../services/urlServices';
import {Constant} from '../constants/enviroment';


class Home {

    private messages: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private email: any = ko.observable();
    private full_name: any = ko.observable();

    public activate() {
        this.isLoading(true);
        setApiUrls().then((resp: boolean) => {
            return getMeInfo();
        }).then((user: IUser) => {
            this.full_name(user.full_name);
            this.messages(this.loadMessages());
            this.isLoading(false);
        }).catch((error: Error) => {
            console.log(error.toString());
            window.location.assign(Constant.DEFAULT_AUTH_URL);
        });
    }

    public loadMessages(): IMessage[] {
        return [{
                title: "Welcome to IWS-TEST",
                content: "Use the navbar menu to move to aother options"
        }];
    }
}


export = Home;