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
        'bootstrap_treeview': '../node_modules/bootstrap-treeview/dist/bootstrap-treeview.min',
        'Sortable': '../node_modules/sortablejs/Sortable.min',
        'ko_sortable': '../node_modules/knockout-sortablejs/knockout-sortable'
    },
  shim: {
    bootstrap: {
            deps: ['jquery'],
            exports: 'jQuery'
        },
    bootstrap_treeview: {
          deps: ['jquery']
      },
      ko_sortable:{
          deps: ['Sortable']
      }
    },

});

define(['durandal/system', 'durandal/app', 'durandal/viewLocator', 'bootstrap', 'bootstrap-datepicker', 'bootstrap_treeview', 'Sortable', 'ko_sortable'],
    function (system, app, viewLocator) {

    system.debug(true);


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