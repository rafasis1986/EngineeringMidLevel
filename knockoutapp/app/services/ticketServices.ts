import * as Q from 'q';
import {IUser} from 'userInterfaces';
import {UrlSingleton} from '../singletons/urlSingleton';
import {Constant} from '../constants/enviroment';
import {AuthSingleton} from '../singletons/authSingleton';
import Deferred = Q.Deferred;
import {} from 'ticketInterface';
import {ITicketBase} from 'ticketInterface';


export function getTickets():  Promise<ITicketBase[]> {
    let deferred: Deferred<ITicketBase[]> = Q.defer<ITicketBase[]>(),
        ajaxSettings: any = {
        'url': UrlSingleton.getInstance().getApiTickets(),
        'method': 'GET',
        'headers': {
            'Authorization': AuthSingleton.getInstance().getToken()
        }};
    $.ajax(ajaxSettings)
        .then((response: any) => {
            let resp: ITicketBase[];
            resp = response.data.map( (request: any) => {
                if (request.type === 'request') {
                    let aux: any = {};
                    aux.id = request.id;
                    aux.detail = request.attributes.detail;
                    aux.created_at = request.attributes.created_at;
                    return aux;
                }
            });
            deferred.resolve(resp);
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}


export function createTicket(ticket: ITicketBase):  Promise<ITicketBase> {
    let deferred: Deferred<ITicketBase> = Q.defer<ITicketBase>(),
        ajaxSettings: any = {
            'url': UrlSingleton.getInstance().getApiTickets(),
            'method': 'POST',
            'headers': {
                'Authorization': AuthSingleton.getInstance().getToken(),
                'content-type': 'application/json'
            },
            'data' : {
                request_id: ticket.request_id,
                detail: ticket.detail
            }
    };
    $.ajax(ajaxSettings)
        .then((response: any) => {
            deferred.resolve({
                id: response.data.id,
                detail: response.data.attributes.detail,
                created_at: response.data.attributes.created_at,
                request_id: response.data.relationships.request.data.id
            });
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}