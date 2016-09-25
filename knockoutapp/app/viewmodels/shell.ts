import * as router from 'plugins/router';
import * as app from 'durandal/app';


let activate = function() {
    router.map([
        { route: '', moduleId: 'viewmodels/home', title: "Home", nav: true },
        { route: 'clients', moduleId: 'viewmodels/clients', title: "Clients", nav: true }
        ]).buildNavigationModel();
    return router.activate();

};

export = { router, activate };