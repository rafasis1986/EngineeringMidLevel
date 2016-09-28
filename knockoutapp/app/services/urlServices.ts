import {getCookie} from './utils';
import {UrlSingleton} from '../singletons/urlSingleton';
import {Constant} from '../env/constants';
import {getEnv} from './envServices';


export function setApiUrls (): boolean {
    let url: string,
        urls: string[],
        response: boolean = false,
        urlObject: any = {},
        singleton: any = UrlSingleton.getInstance();
    
    url = getCookie(Constant.URLS_LABEL);
    if (getEnv() === Constant.PRODUCTION_ENV) {
        singleton.setApiBase(Constant.PRODUCTION_BE_URL);
    } else {
        singleton.setApiBase(Constant.DEVELOPMENT_BE_URL);
    }
    if (url) {
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
            response = true;
        }
    }
    return response;
}
