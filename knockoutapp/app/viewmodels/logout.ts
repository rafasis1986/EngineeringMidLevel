import * as system from 'durandal/system';
import * as app from 'durandal/app';
import {removeAuthToken, getAuthUrl} from '../services/authServices';
import {clearSession} from '../services/utils';
import {UrlSingleton} from "../singletons/urlSingleton";

class Logout {

    public activate() {
        removeAuthToken();
        clearSession();
        window.location.assign(UrlSingleton.getInstance().getAuthUrl());
    }
}

export = Logout;