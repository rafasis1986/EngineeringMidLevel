import * as ko from 'knockout';
import {getMessage} from '../services/messageService';
import {IMessage} from 'messageInterface';

class BaseView {

    protected message: any = ko.observable();

    protected type: any = ko.observable();

    protected displayMessage: any = ko.observable(false);

    constructor () {
        let message: IMessage = getMessage(); 
        if(message != null) {
            this.displayMessage(true);
            this.message(message.content);
            this.type(message.type);
        }
    }
}

export = BaseView;
