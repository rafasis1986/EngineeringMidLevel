define(["require", "exports"], function (require, exports) {
    "use strict";
    var AuthSingleton = (function () {
        function AuthSingleton() {
            this._token = null;
            if (AuthSingleton._instance) {
                throw new Error("Error: Instantiation failed: Use UrlSingleton.getInstance() instead of new.");
            }
            AuthSingleton._instance = this;
        }
        AuthSingleton.getInstance = function () {
            return AuthSingleton._instance;
        };
        AuthSingleton.prototype.setToken = function (value) {
            this._token = value;
        };
        AuthSingleton.prototype.getToken = function () {
            return this._token;
        };
        AuthSingleton._instance = new AuthSingleton();
        return AuthSingleton;
    }());
    exports.AuthSingleton = AuthSingleton;
});
//# sourceMappingURL=authSingleton.js.map