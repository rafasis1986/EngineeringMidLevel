import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import {getAuthToken} from '../services/auth';
import {getAuthUrl} from '../constants/index';
import {IFeature} from 'homeInterfaces';

/**
 * Home VM
 */



class Home {
    public features: any = ko.observableArray();
    public isLoading: any = ko.observable();

    private messageTitle: string = 'Application Message';
    private message: string = 'Hello from your application';

    public activate() {
        this.isLoading(true);
        let token: string = getAuthToken();
        if (! token) {
            window.location.assign(getAuthUrl());
        }
        alert(token);

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
        return system.defer(function(dfd) {
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