var appRoot = 'app/';
var contentRoot = 'css/'
var outputRoot = 'dist/';


module.exports = {
    root: appRoot,
    output:outputRoot,
    source_js: appRoot + '**/*.js',
    source_ts: appRoot + '**/*.ts',
    source_dts:['typings/globals/**/*.d.ts','typings_local/*.d.ts','jspm_packages/**/*.d.ts'],
    html: appRoot + '**/*.html',
    css: contentRoot + '**/*.css'
}