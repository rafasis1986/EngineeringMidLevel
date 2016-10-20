requirejs.config({
    paths: {
        'text': '../node_modules/requirejs-text/text',
        'durandal': '../node_modules/durandal/js',
        'plugins': '../node_modules/durandal/js/plugins',
        'transitions': '../node_modules/durandal/js/transitions',
        'knockout': '../node_modules/knockout/build/output/knockout-latest',
        'jquery': '../node_modules/jquery/dist/jquery.min',
        'bootstrap-datepicker': '../node_modules/bootstrap-datepicker/dist/js/bootstrap-datepicker.min',
        'bootstrap': '../node_modules/bootstrap/dist/js/bootstrap.min',
        'js-cookie': '../node_modules/js-cookie/src/js.cookie',
        'q': '../node_modules/q/q',
        'knockout.validation': '../node_modules/knockout.validation/dist/knockout.validation.min',
        'Sortable': '../node_modules/sortablejs/Sortable.min',
        'ko_sortable': '../node_modules/knockout-sortablejs/knockout-sortable',
        'knockstrap': '../node_modules/knockstrap/build/knockstrap',
    },
  shim: {
    bootstrap: {
            deps: ['jquery'],
            exports: 'jQuery'
        },
      ko_sortable:{
          deps: ['Sortable']
      }
    },

});

define(['durandal/system', 'durandal/app', 'durandal/viewLocator',  'q', 'bootstrap', 'knockstrap', 'bootstrap-datepicker', 'Sortable', 'ko_sortable'],
    function (system, app, viewLocator, Q) {

    system.debug(false);
    system.defer = function (action) {
        var deferred = Q.defer();
        action.call(deferred, deferred);
        var promise = deferred.promise;
        deferred.promise = function() {
            return promise;
        };
        return deferred;
    };


    app.title = "iws-test";

    app.configurePlugins({
        router:true,
        dialog: true,
        widget: true
    });

    app.start().then(function() {
        // Replace 'viewmodels' in the moduleId with 'views' to locate the view.
        // Look for partial views in a 'views' folder in the root.
        viewLocator.useConvention();

        // Show the app by setting the root view model for our application with a transition.
        app.setRoot('viewmodels/shell');
    });
});