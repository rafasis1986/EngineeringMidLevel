var gulp = require('gulp');
var paths = require('./paths');
var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');

    var tslint = require('gulp-tslint');

    gulp.task('tslint', function() {
        return gulp.src(paths.source_ts)
            .pipe(tslint())
            .pipe(tslint.report('prose', {
                emitError: false
            }));
    });



    gulp.task('jshint', function() {
        return gulp.src(paths.source_js)
            .pipe(jshint())
            .pipe(jshint.reporter(stylish));
    });