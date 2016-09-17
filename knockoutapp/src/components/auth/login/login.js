define(["require", "exports", "knockout", "text!./login.html"], function (require, exports, ko) {
    "use strict";
    exports.template = require("text!./login.html");
    exports.API_URL = ' http://localhost:5000/api/1.0/';
    var viewModel = (function () {
        function viewModel(params) {
            this.message = ko.observable('');
            this.userPassword = ko.observable();
            this.userEmail = ko.observable();
            this.erroMessage = ko.observable();
            this.isVisible = ko.observable(true);
            var aux = sessionStorage.getItem('token');
            if (aux) {
                this.isVisible(false);
            }
        }
        viewModel.prototype.goSignUp = function () {
            window.location.assign('#sign-up');
        };
        viewModel.prototype.login = function () {
            var _this = this;
            $.ajax(exports.API_URL + '/auth/', {
                method: 'POST',
                data: {
                    email: this.userEmail,
                    password: this.userPassword
                }
            }).then(function (data) {
                console.log(data);
            }).fail(function (error) {
                _this.erroMessage(error);
            });
        };
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
//# sourceMappingURL=login.js.map