import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import {IFeature} from 'homeInterfaces';
import {setAuthToken} from '../services/authServices';
import {getMeInfo} from '../services/userServices';
import {IUser} from 'userInterfaces';
import {setApiUrls} from '../services/urlServices';
import {Constant} from '../constants/enviroment';


class Home {
    public features: any = ko.observableArray();
    public isLoading: any = ko.observable();
    public email: any = ko.observable();
    public full_name: any = ko.observable();

    public activate() {
        this.isLoading(true);
        setApiUrls().then((resp: boolean) => {
            return getMeInfo();
        }).then((user: IUser) => {
            this.full_name(user.full_name);
            this.features(this.loadFeatures());
            this.isLoading(false);
        }).catch((error: Error) => {
            console.log(error.toString());
            window.location.assign(Constant.DEFAULT_AUTH_URL);
        });
    }

    public loadFeatures(): IFeature[] {
        return [{
                title: "Welcome to IWS-TEST",
                content: "Use the navbar menu to move to aother options"
        }];
    }
}


export = Home;