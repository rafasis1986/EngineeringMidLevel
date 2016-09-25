/**
 * Created by rtorres on 9/25/16.
 */
declare module 'homeInterfaces' {
    export interface IFeature {
        title: string,
        content: string,
        arguments?: string[],
        options?: string[],
        details?: string
    }
}