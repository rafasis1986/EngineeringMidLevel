// This module configures crossroads.js, a routing library. If you prefer, you
// can use any other routing library (or none at all) as Knockout is designed to
// compose cleanly with external libraries.
//
// You *don't* have to follow the pattern established here (each route entry
// specifies a 'page', which is a Knockout component) - there's nothing built into
// Knockout that requires or even knows about this technique. It's just one of
// many possible ways of setting up client-side routes.
define(["require", "exports", 'knockout', 'crossroads', 'hasher'], function (require, exports, ko, crossroads, hasher) {
    "use strict";
    var router;
    (function (router) {
        /**
         * An observable value that changes to represent the current route.
         */
        router.currentRoute = ko.observable({});
        var allRoutes = [
            { url: '', params: { page: 'home-page' } },
            { url: 'about', params: { page: 'about-page' } },
            { url: 'login', params: { page: 'login' } },
            { url: 'sign-up', params: { page: 'sign-up' } }
        ];
        // Register routes with crossroads.js
        ko.utils.arrayForEach(allRoutes, function (route) {
            crossroads.addRoute(route.url, function (requestParams) {
                router.currentRoute(ko.utils.extend(requestParams, route.params));
            });
        });
        // Activate crossroads
        function parseHash(newHash, oldHash) { crossroads.parse(newHash); }
        crossroads.normalizeFn = crossroads.NORM_AS_OBJECT;
        hasher.initialized.add(parseHash);
        hasher.changed.add(parseHash);
        hasher.init();
    })(router || (router = {}));
    return router;
});
//# sourceMappingURL=router.js.map