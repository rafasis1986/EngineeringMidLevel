define(["require", "exports", "knockout", "text!./home.html"], function (require, exports, ko) {
    "use strict";
    exports.template = require("text!./home.html");
    var viewModel = (function () {
        function viewModel() {
            this.message = ko.observable("Welcome to ko-t!");
        }
        viewModel.prototype.doSomething = function () {
            var _this = this;
            var root = 'http://jsonplaceholder.typicode.com';
            var response = '';
            $.ajax(root + '/posts', {
                method: 'POST',
                data: {
                    title: 'foo',
                    body: 'bar',
                    userId: 1
                }
            }).then(function (data) {
                console.log(data);
                $.ajax({
                    url: root + '/posts/1',
                    method: 'GET' })
                    .then(function (data) {
                    console.log(data);
                    _this.message(data.title);
                })
                    .fail(function (error) {
                    console.log(error);
                });
            });
        };
        return viewModel;
    }());
    exports.viewModel = viewModel;
});
//# sourceMappingURL=home.js.map