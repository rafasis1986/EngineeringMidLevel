/**
 * Created by rtorres on 9/24/16.
 */
import {getCookie} from './utils';
import {AUTH_TOKEN} from '../constants/index';

export function getAuthToken (): string {
    return getCookie(AUTH_TOKEN);
}


