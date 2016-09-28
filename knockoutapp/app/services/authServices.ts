/**
 * Created by rtorres on 9/24/16.
 */
import * as Q from 'q';
import {getCookie, deleteCookie} from './utils';
import {AuthSingleton} from '../singletons/authSingleton';
import {Constant} from '../constants/enviroment';
import Deferred = Q.Deferred;


export function setAuthToken ():  Promise<boolean> {
    let deferred: Deferred<boolean> = Q.defer<boolean>(),
        token: string,
        singleton: any;
    token = getCookie(Constant.AUTH_LABEL);
    if (!token) {
        deferred.reject('Auth token does not exist');
    } else {
        singleton = AuthSingleton.getInstance();
        singleton.setToken(Constant.TYPE_TOKEN + ' ' + token);
        deferred.resolve(true);
    }

    return deferred.promise;
}

export function removeAuthToken ():  void {
    deleteCookie(Constant.AUTH_LABEL);
}
