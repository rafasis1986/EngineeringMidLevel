/**
 * Created by rtorres on 9/25/16.
 */
declare module 'userInterfaces' {
    export interface IUser {
        email: string,
        first_name: string,
        last_name: string,
        full_name?: string,
        id: string
    }
}