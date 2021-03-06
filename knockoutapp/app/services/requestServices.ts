import * as Q from 'q';
import {IUser} from 'userInterfaces';
import {UrlSingleton} from '../singletons/urlSingleton';
import {Constant} from '../constants/enviroment';
import {AuthSingleton} from '../singletons/authSingleton';
import Deferred = Q.Deferred;
import {IRequestBase, IRequest} from 'requestInterface';
import {ICreateRequest} from "requestInterface";
import {IUpdateRequest} from "requestInterface";


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

export function getPendingRequests():  Promise<IRequestBase[]> {
    let deferred: Deferred<IRequestBase[]> = Q.defer<IRequestBase[]>(),
        ajaxSettings: any = {
            'url': UrlSingleton.getInstance().getApiPendings(),
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

export function createRequest(request: ICreateRequest):  Promise<ICreateRequest> {
    let deferred: Deferred<ICreateRequest> = Q.defer<ICreateRequest>(),
        data: any,
        ajaxSettings: any;

    data = {
        client: request.client,
        client_priority: request.client_priority,
        details: request.details,
        product_area: request.product_area,
        target_date: request.target_date,
        ticket_url: request.ticket_url,
        title: request.title

    };
    ajaxSettings = {
        'url': UrlSingleton.getInstance().getApiRequests(),
        'method': 'POST',
        'headers': {
            'Authorization': AuthSingleton.getInstance().getToken(),
            'Content-Type': 'application/json'
        },
        'data' : JSON.stringify(data)
    };
    $.ajax(ajaxSettings)
        .then((response: any) => {
            deferred.resolve({
                client: response.data.relationships.client.data.id,
                client_priority: response.data.attributes.client_priority.toString(),
                details: response.data.attributes.description,
                product_area: response.data.attributes.product_area,
                target_date: response.data.attributes.target_date,
                title: response.data.attributes.title,
                ticket_url: response.data.attributes.ticket_url,
                id: response.data.id
            });
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}

export function updateRequest(request: IUpdateRequest, requestPath: string):  Promise<ICreateRequest> {
    let deferred: Deferred<ICreateRequest> = Q.defer<ICreateRequest>(),
        data: any,
        ajaxSettings: any;

    data = {
        client_priority: request.client_priority,
        details: request.details,
        product_area: request.product_area,
        target_date: request.target_date,
        ticket_url: request.ticket_url,
        title: request.title
    };
    ajaxSettings = {
        'url': UrlSingleton.getInstance().getApiBase() + requestPath,
        'method': 'PUT',
        'headers': {
            'Authorization': AuthSingleton.getInstance().getToken(),
            'Content-Type': 'application/json'
        },
        'data' : JSON.stringify(data)
    };
    $.ajax(ajaxSettings)
        .then((response: any) => {
            deferred.resolve({
                client: response.data.relationships.client.data.id,
                client_priority: response.data.attributes.client_priority.toString(),
                details: response.data.attributes.description,
                product_area: response.data.attributes.product_area,
                target_date: response.data.attributes.target_date,
                title: response.data.attributes.title,
                ticket_url: response.data.attributes.ticket_url,
                id: response.data.id
            });
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}

export function updateRequestPriorityList(orderList: number[]):  Promise<IRequestBase[]> {
    let deferred: Deferred<IRequestBase[]> = Q.defer<IRequestBase[]>(),
        data: any,
        ajaxSettings: any;

    data = {
        requests_id: orderList
    };
    ajaxSettings = {
        'url': UrlSingleton.getInstance().getApiPendings(),
        'method': 'POST',
        'headers': {
            'Authorization': AuthSingleton.getInstance().getToken(),
            'Content-Type': 'application/json'
        },
        'data' : JSON.stringify(data)
    };
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

export function deleteRequest(requestPath: string):  Promise<boolean> {
    let deferred: Deferred<boolean> = Q.defer<boolean>(),
        ajaxSettings: any = {
            'url': UrlSingleton.getInstance().getApiBase() + requestPath,
            'method': 'DELETE',
            'headers': {
                'Authorization': AuthSingleton.getInstance().getToken()
            }};
    $.ajax(ajaxSettings)
        .then((response: any) => {
            console.log('borrado');
            console.log(response);
            deferred.resolve(true);
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}