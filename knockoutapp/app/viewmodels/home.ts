import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import {IFeature} from 'homeInterfaces';
import {setAuthToken} from "../services/authServices";
import {Constant} from "../constants/enviroment";
import {getMeInfo} from "../services/userServices";
import {IUser} from "userInterfaces";
import {UrlSingleton} from "../singletons/urlSingleton";
import {setApiUrls} from "../services/urlServices";

/**
 * Home VM
 */



class Home {
    public features: any = ko.observableArray();
    public isLoading: any = ko.observable();
    public email: any = ko.observable();
    public first_name: any = ko.observable();

    private messageTitle: string = 'Application Message';
    private message: string = 'Hello from your application';

    public activate() {
        let aux: boolean;
        this.isLoading(true);
        if(! setApiUrls() || ! setAuthToken()){
            window.location.assign(UrlSingleton.getInstance().getApiBase());
        }

        getMeInfo().then((user:IUser) => {
            this.email(user.email);
        }).catch((error: Error) => {
            console.log(error);
        });
        return this.loadFeatures().then((data) => {

            this.features(data);
            this.isLoading(false);
        });

    }

    public viewDetail(featureData: IFeature) {
        //window.location.assign('#clients');
        //window.location.assign('http://www.google.com');
        console.log(featureData);
        return app.showMessage(featureData.details, featureData.title);
    }

    public loadFeatures(): JQueryDeferred<IFeature[]> {
        return system.defer((dfd: any) => {
            setTimeout(function() {
                dfd.resolve([
                    {
                        title: "Create A ViewModel",
                        content: "Creating a viewmodel is as easy as calling <strong>yo durandal2:viewmodel.</strong>",
                        arguments:['{name}','{typescript|es5}'],
                        options:['--transient'],
                        details:"Providing the --transient flag will generate a viewmodel with a transient lifecyle."
                    },
                    {
                        title: "Run A Task",
                        content: "Run a preconfigured gulp task like <strong>gulp watch.</strong>",
                        arguments:['{taskName}'],
                        details:"Tasks are found in the tasks directory under the project root."
                    }
                ]);
            }, 500);
        });
    }
}


export = Home;