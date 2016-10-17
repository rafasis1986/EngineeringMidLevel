import * as router from 'plugins/router';
import * as app from 'durandal/app';
import {setAuthToken} from '../services/authServices';
import {Constant} from '../constants/enviroment';
import {setApiUrls} from '../services/urlServices';
import {getMeInfo} from '../services/userServices';
import {IUser} from 'userInterfaces';
import * as userSession from '../singletons/userSession';


let activate = function() {
    let nav: any[] = [];
    setAuthToken().then((resp: boolean) => {
        return setApiUrls();
    }).then((resp: any) => {
        return getMeInfo();
    }).then((user: IUser) => {
        userSession.setUserEmail(user.email);
        userSession.setUserFullName(user.full_name);
        userSession.setUserRoles(user.roles.join());
        nav = nav.concat({ route: '', moduleId: 'viewmodels/home', title: 'Home', nav: true });
        if ( userSession.getUserRoles().search(Constant.ROLE_EMPLOYEE) != -1) {
            nav = nav.concat({ route: 'clients', moduleId: 'viewmodels/clients', title: 'Clients', nav: true });
        }
        if ( userSession.getUserRoles().search(Constant.ROLE_CLIENT) != -1) {
            nav = nav.concat({ route: 'request_create', moduleId: 'viewmodels/requestCreate' });
        }
        nav = nav.concat({ route: 'requests', moduleId: 'viewmodels/requests', title: 'Requests', nav: true });
        nav = nav.concat({ route: 'tickets', moduleId: 'viewmodels/tickets', title: 'Tickets', nav: true });
        nav = nav.concat({ route: 'phone', moduleId: 'viewmodels/phone', title: 'Change Phone', nav: false });
        nav = nav.concat({ route: 'logout', moduleId: 'viewmodels/logout', title: 'Logout', nav: false });
        router.map(nav).buildNavigationModel();
        return router.activate();
    }).catch((err: Error) => {
        console.log(err.toString());
        window.location.assign(Constant.DEFAULT_AUTH_URL);
    });

};

export = { router, activate };