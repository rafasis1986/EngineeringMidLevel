/**
 * Created by rtorres on 10/3/16.
 */

declare module 'ticketInterface' {
    export interface ITicketBase {
        id: number,
        detail: string,
        created_at: string,
        request_id: number
    }
}
