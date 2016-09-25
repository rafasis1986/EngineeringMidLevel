var gulp = require('gulp');
var runSequence = require('run-sequence');
var changed = require('gulp-changed');
var plumber = require('gulp-plumber');
var sourcemaps = require('gulp-sourcemaps');
var paths = require('./paths.js');


var typescript = require('gulp-tsb');
var typescriptCompiler = typescriptCompiler || null;
gulp.task('build-ts', function () {
    if (!typescriptCompiler) {
        typescriptCompiler = typescript.create(require('../tsconfig.json').compilerOptions);
    }
    
    return gulp.src(paths.source_dts.concat(paths.source_ts))
        .pipe(plumber())
        .pipe(sourcemaps.init({ loadMaps: true }))
        .pipe(typescriptCompiler())
        .pipe(sourcemaps.write({ includeContent: false,sourceRoot: '/app' }))
        .pipe(gulp.dest(paths.output));
});



//minifies javascript files and includes sourcemaps
gulp.task('build-js', function() {
    return gulp.src(paths.source_js)
        .pipe(plumber())
        .pipe(changed(paths.output, { extension: '.js' }))
        .pipe(gulp.dest(paths.output));
});

// copies changed html files to the output directory
gulp.task('build-html', function() {
    return gulp.src(paths.html)
        .pipe(changed(paths.output, { extension: '.html' }))
        .pipe(gulp.dest(paths.output));
});

// copies changed css files to the output directory
gulp.task('build-css', function() {
    return gulp.src(paths.css)
        .pipe(changed(paths.output, { extension: '.css' }))
        .pipe(gulp.dest(paths.output));
});




// this task calls the clean task (located
// in ./clean.js), then runs the build-system
// and build-html tasks in parallel
// https://www.npmjs.com/package/gulp-run-sequence
gulp.task('build', function(callback) {
    return runSequence(
        'clean',
        'build-js',
        'build-ts',
        ['build-html', 'build-css'],
        callback
    );
});
