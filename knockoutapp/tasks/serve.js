var gulp = require('gulp');
var browserSync = require('browser-sync');

// this task utilizes the browsersync plugin
// to create a dev server instance
// at http://localhost:9000
gulp.task('serve', ['build'], function(done) {
    //How To reset broken NPM on windows:https://github.com/felixrieseberg/npm-windows-upgrade

    //http://stackoverflow.com/questions/25410284/gulp-browser-sync-redirect-api-request-via-proxy
    browserSync({
        online: false,
        open: false,
        port: 9000,
        server: {
            baseDir: ['.'],
            middleware: [
                function(req, res, next) {
                    res.setHeader('Access-Control-Allow-Origin', '*');
                    next();
                }]
        }
    }, done);
});