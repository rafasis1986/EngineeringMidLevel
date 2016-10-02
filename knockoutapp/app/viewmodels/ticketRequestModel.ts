import * as ko from 'knockout';

class TicketRequestModel {

    protected detail: any = ko.observable();

    constructor () {}

    public send(){
        alert('epale');
    }
}

export = TicketRequestModel;
