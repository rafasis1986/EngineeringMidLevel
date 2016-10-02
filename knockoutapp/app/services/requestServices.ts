import * as Q from 'q';
import {IUser} from 'userInterfaces';
import {UrlSingleton} from '../singletons/urlSingleton';
import {Constant} from '../constants/enviroment';
import {AuthSingleton} from '../singletons/authSingleton';
import Deferred = Q.Deferred;
import {IRequestBase, IRequest} from 'requestInterface';


export function getRequests():  Promise<IRequestBase[]> {
    let deferred: Deferred<IRequestBase[]> = Q.defer<IRequestBase[]>(),
        ajaxSettings: any = {
        'url': UrlSingleton.getInstance().getApiRequests(),
        'method': 'GET',
        'headers': {
            'Authorization': AuthSingleton.getInstance().getToken()
        }};
    $.ajax(ajaxSettings)
        .then((response: any) => {
            let resp: IRequestBase[];
            resp = response.data.map( (request: any) => {
                if (request.type === 'request') {
                    let aux: any = {};
                    aux.id = request.id;
                    aux.attended = request.attributes.attended;
                    aux.client_id = request.relationships.client.data.id;
                    aux.client_link = request.relationships.client.links.related;
                    aux.client_priority = request.attributes.client_priority;
                    aux.link = request.links.self;
                    aux.product_area = request.attributes.product_area;
                    aux.target_date = request.attributes.target_date;
                    aux.title = request.attributes.title;
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


export function getRequestDetails(requestPath: string):  Promise<IRequest> {
    let deferred: Deferred<IRequest> = Q.defer<IRequest>(),
        ajaxSettings: any = {
            'url': UrlSingleton.getInstance().getApiBase() + requestPath,
            'method': 'GET',
            'headers': {
                'Authorization': AuthSingleton.getInstance().getToken()
            }};
    $.ajax(ajaxSettings)
        .then((request: any) => {
            deferred.resolve({
                id: request.data.id,
                attended: request.data.attributes.attended,
                attended_date: request.data.attributes.attended_date,
                client_id: request.data.relationships.client.data.id,
                client_link: request.data.relationships.client.links.related,
                client_priority: request.data.attributes.client_priority,
                created_at: request.data.attributes.created_at,
                description: request.data.attributes.description,
                link: request.data.links.self,
                product_area: request.data.attributes.product_area,
                target_date: request.data.attributes.target_date,
                ticket_url: request.data.attributes.ticket_url,
                title: request.data.attributes.title
            });
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}