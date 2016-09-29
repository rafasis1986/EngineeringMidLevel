import * as Q from 'q';
import {IUser} from 'userInterfaces';
import {UrlSingleton} from '../singletons/urlSingleton';
import {Constant} from '../constants/enviroment';
import {AuthSingleton} from '../singletons/authSingleton';
import Deferred = Q.Deferred;

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
            deferred.resolve(user);
        })
        .fail((error: Error) => {
            deferred.reject(error);
        });

    return deferred.promise;
}
