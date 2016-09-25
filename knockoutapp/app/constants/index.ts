/**
 * Created by rtorres on 9/24/16.
 */

export const AUTH_TOKEN: string = 'Authorization';
export const BACKEND_URL: string = 'localhost:5000';

export function getApiUrl (): string {
    return 'http://api.' + BACKEND_URL;
}

export function getAuthUrl (): string {
    return 'http://' + BACKEND_URL + '/auth/';
}
