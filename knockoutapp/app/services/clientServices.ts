import * as Q from 'q';
import {IUser} from 'userInterfaces';
import {UrlSingleton} from '../singletons/urlSingleton';
import {Constant} from '../constants/enviroment';
import {AuthSingleton} from '../singletons/authSingleton';
import Deferred = Q.Deferred;
import {IClient} from "clientInterfaces";


export function getClients():  Promise<IClient[]> {
    let deferred: Deferred<IClient[]> = Q.defer<IClient[]>(),
        ajaxSettings: any = {
        'url': UrlSingleton.getInstance().getApiClients(),
        'method': 'GET',
        'headers': {
            'Authorization': AuthSingleton.getInstance().getToken()
        }};
    $.ajax(ajaxSettings)
        .then((response: any) => {
            let resp: IClient[];
            resp = response.data.map( (client: any) => {
                if (client.type === 'client') {
                    let aux: any = {};
                    aux.email = client.attributes.email;
                    aux.full_name = client.attributes.full_name;
                    aux.id = client.id;
                    aux.link = client.links.self;
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
