/**
 * Created by rtorres on 9/25/16.
 */
declare module 'requestInterface' {
    export interface IRequestBase {
        id: number,
        attended: boolean,
        client_id: number,
        client_link: string,
        client_priority: number,
        link: string,
        product_area: string,
        target_date: string,
        title: string
    }

    export interface IRequest extends IRequestBase{
        attended_date: string,
        client ?: any,
        created_at: string,
        description: string,
        ticket_url:  string,
    }

    export interface ICreateRequest{
        client: string,
        client_priority: string,
        details: string,
        product_area: string,
        target_date: string,
        ticket_url: string,
        title: string
    }

}