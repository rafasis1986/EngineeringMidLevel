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
        'url': UrlSingleton.getInstance().getApiTickets() + 'me',
        'method': 'GET',
        'headers': {
            'Authorization': AuthSingleton.getInstance().getToken()
        }};
    $.ajax(ajaxSettings)
        .then((response: any) => {
            let resp: ITicketBase[];
            resp = response.data.map( (request: any) => {
                if (request.type === 'ticket') {
                    let aux: any = {};
                    aux.id = request.id;
                    aux.created_at = request.attributes.created_at;
                    aux.link = request.links.self;
                    aux.request_title = request.relationships.request.data.id;
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
        data: any,
        ajaxSettings: any;

        data = {
            request_id: ticket.request_id,
            detail: ticket.detail
        };
        ajaxSettings= {
            'url': UrlSingleton.getInstance().getApiTickets(),
            'method': 'POST',
            'headers': {
                'Authorization': AuthSingleton.getInstance().getToken(),
                'Content-Type': 'application/json'
            },
            'data' : JSON.stringify(data)
    };
    $.ajax(ajaxSettings)
        .then((response: any) => {
            // TODO: refactory BE response
            deferred.resolve({
                id: response.data.id,
                detail: response.data.attributes.detail,
                created_at: response.data.attributes.created_at,
                request_id: response.data.relationships.request.data.id,
                link: ''
            });
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}