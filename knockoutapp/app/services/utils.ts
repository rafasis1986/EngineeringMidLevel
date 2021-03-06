/**
 * Created by rtorres on 9/25/16.
 */
import * as Q from 'q';
import * as Cookies from 'js-cookie';

import Deferred = Q.Deferred;

import {IArea} from 'areaInterfaces';
import {UrlSingleton} from '../singletons/urlSingleton';
import {AuthSingleton} from '../singletons/authSingleton';

export function getCookie(cname: string): string {
    return Cookies.get(cname);
}

export function deleteCookie(cname: string): void {
    Cookies.remove(cname);
}

export function getSession(name: string): string {
    return sessionStorage.getItem(name);
}

export function setSession(name: string, value: string): void{
    return sessionStorage.setItem(name, value);
}

export function deleteSession(name: string): void {
    return sessionStorage.removeItem(name);
}

export function clearSession(): void {
    return sessionStorage.clear();
}

export function getAreas():  Promise<IArea[]> {
    let deferred: Deferred<IArea[]> = Q.defer<IArea[]>(),
        user: any = {},
        ajaxSettings: any = {
        'url': UrlSingleton.getInstance().getApiAreas(),
        'method': 'GET',
        'headers': {
            'Authorization': AuthSingleton.getInstance().getToken()
        }};

        $.ajax(ajaxSettings)
        .then((response: any) => {
            deferred.resolve(response);
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}
