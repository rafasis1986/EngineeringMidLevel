/**
 * Created by rtorres on 10/18/16.
 */
declare module 'treeNodeInterfaces' {
    export interface INode {
        text: string,
        href: string,
        tags: any[],
        nodes?: any[]
    }
}