import * as system from 'durandal/system';
import * as app from 'durandal/app';
import {setAuthToken, removeAuthToken} from '../services/authServices';
import {UrlSingleton} from '../singletons/urlSingleton';

class Logout {

    public activate() {
        removeAuthToken();
        window.location.assign(UrlSingleton.getInstance().getAuthUrl());
    }
}

export = Logout;