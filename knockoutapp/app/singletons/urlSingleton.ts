import {Constant} from '../constants/enviroment';

class UrlSingleton {

    private static _instance:UrlSingleton = new UrlSingleton();

    private _api_users: string = null;

    private _api_clients: string = null;

    private _api_requests: string = null;

    private _api_tickets: string = null;

    private _api_base: string = null;

    constructor() {
        if(UrlSingleton._instance){
            throw new Error("Error: Instantiation failed: Use UrlSingleton.getInstance() instead of new.");
        }
        UrlSingleton._instance = this;
    }

    public static getInstance(): UrlSingleton{
        return UrlSingleton._instance;
    }

    public setApiBase(value: string): void{
        this._api_base = value;
    }

    public getApiBase(): string {
        return this._api_base;
    }

    public getAuthUrl(): string {
        return this._api_base + Constant.AUTH_PATH;
    }

    public setApiUsers(value: string): void{
        this._api_users = this._api_base + value;
    }

    public getApiUsers(): string {
        return this._api_users;
    }

    public setApiClients(value: string): void{
        this._api_clients = this._api_base + value;
    }

    public getApiClients(): string {
        return this._api_clients;
    }

    public setApiRequests(value: string): void{
        this._api_requests = this._api_base + value;
    }

    public getApiRequests(): string {
        return this._api_requests;
    }

    public setApiTickets(value: string): void {
        this._api_tickets = this._api_base + value;
    }

    public getApiTickets(): string {
        return this._api_tickets;
    }

}

export {UrlSingleton}
