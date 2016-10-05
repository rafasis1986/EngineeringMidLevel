import {Constant} from '../constants/enviroment';
import {IMessage} from 'messageInterface';

export function makeMessage(message:string, type:string): void {
    sessionStorage.setItem(Constant.MESSAGE, 'true');
    sessionStorage.setItem(Constant.MESSAGE_CONTENT, message);
    sessionStorage.setItem(Constant.MESSAGE_TYPE, type);
}

export function getMessage(): IMessage {
    let message: any = {};

    if (sessionStorage.getItem(Constant.MESSAGE) === 'true') {
        message = {
            content: sessionStorage.getItem(Constant.MESSAGE_CONTENT),
            type: sessionStorage.getItem(Constant.MESSAGE_TYPE)
        };
        deleteMessage();
        return message;
    }

    return null;
}

export function deleteMessage(): void {
    sessionStorage.removeItem(Constant.MESSAGE);
    sessionStorage.removeItem(Constant.MESSAGE_CONTENT);
    sessionStorage.removeItem(Constant.MESSAGE_TYPE);
}
