/**
 * Created by rtorres on 9/25/16.
 */


export function getCookie(cname: string): string {
    let name: string = cname + '=';
    let ca: string[] = document.cookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        let c: any = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length,c.length);
        }
    }
    return null;
}