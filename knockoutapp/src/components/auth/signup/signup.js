define(["require", "exports", 'knockout', "text!./signup.html"], function (require, exports, ko) {
    "use strict";
    var template = require('text!./signup.html');
    exports.template = template;
    var API_URL = ' http://localhost:5000/api/1.0/';
    var viewModel = (function () {
        function viewModel(params) {
            this.userPassword = ko.observable();
            this.userName = ko.observable();
            this.userEmail = ko.observable();
            this.erroMessage = ko.observable();
            this.isVisible = ko.observable(true);
            var aux = sessionStorage.getItem('token');
            if (aux) {
                this.isVisible(false);
            }
        }
        viewModel.prototype.signUp = function () {
            var _this = this;
            $.ajax(API_URL + 'users/', {
                method: 'POST',
                data: {
                    username: this.userName,
                    email: this.userEmail,
                    password: this.userPassword
                }
            }).then(function (data) {
                console.log(data);
            }).fail(function (error) {
                _this.erroMessage(error);
            });
        };
        return viewModel;
    }());
    exports.viewModel = viewModel;
});
//# sourceMappingURL=signup.js.map