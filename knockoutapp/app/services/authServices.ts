/**
 * Created by rtorres on 9/24/16.
 */
import {getCookie} from './utils';

import {AuthSingleton} from '../singletons/authSingleton';
import {Constant} from '../env/constants';


export function setAuthToken (): boolean {
    let token: string,
        singleton: any;
    token = getCookie(Constant.AUTH_LABEL);
    if (!token) {
        return false;
    } else {
        singleton = AuthSingleton.getInstance();
        singleton.setToken(Constant.TYPE_TOKEN + ' ' + token);
    }

    return true;
}

