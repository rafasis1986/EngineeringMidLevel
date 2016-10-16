import * as system from 'durandal/system';
import * as app from 'durandal/app';
import {removeAuthToken} from '../services/authServices';
import {UrlSingleton} from '../singletons/urlSingleton';
import {clearSession} from '../services/utils';

class Logout {

    public activate() {
        removeAuthToken();
        clearSession();
        window.location.assign(UrlSingleton.getInstance().getAuthUrl());
    }
}

export = Logout;