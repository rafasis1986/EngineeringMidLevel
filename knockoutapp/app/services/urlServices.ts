import * as Q from 'q';
import {getCookie} from './utils';
import {UrlSingleton} from '../singletons/urlSingleton';
import {Constant} from '../constants/enviroment';
import {getEnv} from './envServices';
import Deferred = Q.Deferred;

export function setApiUrls (): Promise<boolean> {
    let deferred: Deferred<boolean> = Q.defer<boolean>(),
        url: string,
        urls: string[],
        urlObject: any = {},
        singleton: any = UrlSingleton.getInstance();

    url = getCookie(Constant.URLS_LABEL);
    if (! url) {
        deferred.reject('Missed Api Urls');
    } else {
        if (getEnv() === Constant.PRODUCTION_ENV) {
            singleton.setApiBase(Constant.PRODUCTION_BE_URL);
        } else {
            singleton.setApiBase(Constant.DEVELOPMENT_BE_URL);
        }
        url = url.replace('\"', '');
        urls = url.replace('"', '').split(Constant.CHARACTER_PARTITION);
        if (urls.length > 0) {
            for (var i = 0; i < urls.length; i++) {
                if (urls[i].length > 1) {
                    let aux: string[] = urls[i].split(':');
                    urlObject[aux[0]] = aux[1];
                }
            }
            if (urlObject[Constant.USERS_API]) {
                singleton.setApiUsers(urlObject[Constant.USERS_API]);
            }
            if (urlObject[Constant.CLIENTS_API]) {
                singleton.setApiClients(urlObject[Constant.CLIENTS_API]);
            }
            if (urlObject[Constant.REQUESTS_API]) {
                singleton.setApiRequests(urlObject[Constant.REQUESTS_API]);
            }
            if (urlObject[Constant.TICKETS_API]) {
                singleton.setApiTickets(urlObject[Constant.TICKETS_API]);
            }
            if (urlObject[Constant.AREAS_API]) {
                singleton.setApiAreas(urlObject[Constant.AREAS_API]);
            }

            deferred.resolve(true);
        } else {
            deferred.reject('Missed the api Urls.');
        }
    }

    return deferred.promise;
}
