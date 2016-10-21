import * as Q from 'q';
import {IUser} from 'userInterfaces';
import {UrlSingleton} from '../singletons/urlSingleton';
import {Constant} from '../constants/enviroment';
import {AuthSingleton} from '../singletons/authSingleton';
import Deferred = Q.Deferred;
import {setSession} from "./utils";

export function getMeInfo():  Promise<IUser> {
    let deferred: Deferred<IUser> = Q.defer<IUser>();
    let user: any = {},
        ajaxSettings: any = {
        'url': UrlSingleton.getInstance().getApiUsers() + Constant.USERS_API_ME,
        'method': 'GET',
        'headers': {
            'Authorization': AuthSingleton.getInstance().getToken()
        }};
    $.ajax(ajaxSettings)
        .then((response: any) => {
            console.log(response);
            user.email = response.data.attributes.email;
            user.first_name = response.data.attributes.first_name;
            user.last_name = response.data.attributes.last_name;
            user.full_name = response.data.attributes.full_name;
            user.roles = response.data.relationships.roles.data.map( (role: any) => {
                return role.id;
            });
            deferred.resolve(user);
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}

export function updateUser(phone: string):  Promise<string> {
    let deferred: Deferred<string> = Q.defer<string>();
    let user: any = {},
        ajaxSettings: any = {
            'url': UrlSingleton.getInstance().getApiUsers() + Constant.USERS_API_ME,
            'method': 'PATCH',
            'headers': {
                'Authorization': AuthSingleton.getInstance().getToken(),
                'Content-Type': 'application/json'
            },
            'data' : JSON.stringify({ phone_number: phone})
    };
    $.ajax(ajaxSettings)
        .then((response: any) => {
            console.log(response);
            deferred.resolve(response.message);
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}

export function confirmUpdateUser(code: string):  Promise<IUser> {
    let deferred: Deferred<IUser> = Q.defer<IUser>();
    let user: any = {},
        ajaxSettings: any = {
            'url': UrlSingleton.getInstance().getApiUsers() + Constant.USERS_API_ME,
            'method': 'PUT',
            'headers': {
                'Authorization': AuthSingleton.getInstance().getToken(),
                'Content-Type': 'application/json'
            },
            'data' : JSON.stringify({ code: code})
    };
    $.ajax(ajaxSettings)
        .then((response: any) => {
            user.email = response.data.attributes.email;
            user.phone_number = response.data.attributes.phone_number;
            user.first_name = response.data.attributes.first_name;
            user.last_name = response.data.attributes.last_name;
            user.full_name = response.data.attributes.full_name;
            user.roles = response.data.relationships.roles.data.map( (role: any) => {
                return role.id;
            });
            deferred.resolve(user);
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}
