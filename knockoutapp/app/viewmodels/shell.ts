import * as router from 'plugins/router';
import * as app from 'durandal/app';
import {setAuthToken} from '../services/authServices';
import {Constant} from '../constants/enviroment';
import {setApiUrls} from '../services/urlServices';


let activate = function() {
    setAuthToken().then((resp: boolean) => {
        return setApiUrls();
    }).then((resp) => {
        console.log('Succes Auth!');
    }).catch((err: Error) => {
        console.log(err.toString());
        window.location.assign(Constant.DEFAULT_AUTH_URL);
    });
    router.map([
        { route: '', moduleId: 'viewmodels/home', title: 'Home', nav: true },
        { route: 'clients', moduleId: 'viewmodels/clients', title: 'Clients', nav: true },
        { route: 'requests', moduleId: 'viewmodels/requests', title: 'Requests', nav: true },
        { route: 'request_create', moduleId: 'viewmodels/requestCreate' },
        { route: 'tickets', moduleId: 'viewmodels/tickets', title: 'Tickets', nav: true },
        { route: 'logout', moduleId: 'viewmodels/logout', title: 'Logout', nav: false }
        ]).buildNavigationModel();
    return router.activate();

};

export = { router, activate };