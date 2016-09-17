define(["require", "exports", "knockout", "bootstrap", "./router", 'tether'], function (require, exports, ko, bootstrap, router) {
    "use strict";
    var bs = bootstrap;
    // Components can be packaged as AMD modules, such as the following:
    ko.components.register('nav-bar', { require: 'components/nav-bar/nav-bar' });
    ko.components.register('home-page', { require: 'components/home-page/home' });
    ko.components.register('login', { require: 'components/auth/login/login' });
    ko.components.register('sign-up', { require: 'components/auth/signup/signup' });
    // ... or for template-only components, you can just point to a .html file directly:
    ko.components.register('about-page', {
        template: { require: 'text!components/about-page/about.html' }
    });
    // [Scaffolded component registrations will be inserted here. To retain this feature, don't remove this comment.]
    // Start the application
    ko.applyBindings({ route: router.currentRoute });
});
//# sourceMappingURL=startup.js.map