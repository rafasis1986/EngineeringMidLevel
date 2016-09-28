define(["require", "exports"], function (require, exports) {
    "use strict";
    var UrlSingleton = (function () {
        function UrlSingleton() {
            this._api_users = null;
            this._api_clients = null;
            this._api_requests = null;
            if (UrlSingleton._instance) {
                throw new Error("Error: Instantiation failed: Use UrlSingleton.getInstance() instead of new.");
            }
            UrlSingleton._instance = this;
        }
        UrlSingleton.getInstance = function () {
            return UrlSingleton._instance;
        };
        UrlSingleton.prototype.setApiUsers = function (value) {
            this._api_users = value;
        };
        UrlSingleton.prototype.getApiUsers = function () {
            return this._api_users;
        };
        UrlSingleton.prototype.setApiClients = function (value) {
            this._api_clients = value;
        };
        UrlSingleton.prototype.getApiClients = function () {
            return this._api_users;
        };
        UrlSingleton.prototype.setApiRequests = function (value) {
            this._api_users = value;
        };
        UrlSingleton.prototype.getApiRequests = function () {
            return this._api_users;
        };
        UrlSingleton._instance = new UrlSingleton();
        return UrlSingleton;
    }());
    exports.UrlSingleton = UrlSingleton;
});
//# sourceMappingURL=urlSingleton.js.map