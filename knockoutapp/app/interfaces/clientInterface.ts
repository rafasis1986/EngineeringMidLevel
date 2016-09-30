/**
 * Created by rtorres on 9/25/16.
 */
declare module 'clientInterfaces' {
    export interface IClient {
        email: string,
        full_name: string,
        link: string,
        id: number,
        first_name ?: string,
        last_name ?: string,
        created_at ?: string
    }
}