/**
 * Created by rtorres on 9/25/16.
 */
import * as Cookies from 'js-cookie';

export function getCookie(cname: string): string {
    return Cookies.get(cname);
}