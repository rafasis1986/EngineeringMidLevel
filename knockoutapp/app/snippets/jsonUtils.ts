/**
 * Created by rtorres on 10/1/16.
 */

export function findPositionJsonArray(array: any[], key: string, value: any): number{
    let iter: number = 0;

    for(iter; iter < array.length; iter++) {
        if (array[iter][key] == value){
            return iter;
        }
    }

    return -1;
}
