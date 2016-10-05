/**
 * Created by rtorres on 9/27/16.
 */

class AuthSingleton {

    private static _instance:AuthSingleton = new AuthSingleton();

    private _token: string = null;

    constructor() {
        if(AuthSingleton._instance){
            throw new Error("Error: Instantiation failed: Use UrlSingleton.getInstance() instead of new.");
        }
        AuthSingleton._instance = this;
    }

    public static getInstance(): AuthSingleton{
        return AuthSingleton._instance;
    }

    public setToken(value: string): void{
        this._token = value;
    }

    public getToken(): string {
        return this._token;
    }

}

export {AuthSingleton}