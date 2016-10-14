import * as router from 'plugins/router';
import * as app from 'durandal/app';
import {setAuthToken} from '../services/authServices';
import {Constant} from '../constants/enviroment';
import {setApiUrls} from '../services/urlServices';
import {getMeInfo} from '../services/userServices';
import {IUser} from 'userInterfaces';
import {UserSingleton} from '../singletons/userSingleton';


let activate = function() {
    setAuthToken().then((resp: boolean) => {
        return setApiUrls();
    }).then((resp: any) => {
        return getMeInfo();
    }).then((user: IUser) => {
        UserSingleton.setEmail(user.email);
        UserSingleton.setFullName(user.full_name);
        UserSingleton.setRoles(user.roles.join());
    }).catch((err: Error) => {
        console.log(err.toString());
        window.location.assign(Constant.DEFAULT_AUTH_URL);
    });
    let nav: any[] = [];
    nav = nav.concat({ route: '', moduleId: 'viewmodels/home', title: 'Home', nav: true });
    if ( UserSingleton.getRoles().search(Constant.ROLE_EMPLOYEE) != -1) {
        nav = nav.concat({ route: 'clients', moduleId: 'viewmodels/clients', title: 'Clients', nav: true });
    }
    if ( UserSingleton.getRoles().search(Constant.ROLE_CLIENT) != -1) {
        nav = nav.concat({ route: 'request_create', moduleId: 'viewmodels/requestCreate' });
    }
    nav = nav.concat({ route: 'requests', moduleId: 'viewmodels/requests', title: 'Requests', nav: true });
    nav = nav.concat({ route: 'tickets', moduleId: 'viewmodels/tickets', title: 'Tickets', nav: true });
    nav = nav.concat({ route: 'logout', moduleId: 'viewmodels/logout', title: 'Logout', nav: false });
    router.map(nav).buildNavigationModel();
    return router.activate();

};

export = { router, activate };