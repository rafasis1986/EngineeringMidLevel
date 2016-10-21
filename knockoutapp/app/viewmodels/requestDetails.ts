import {IRequest} from 'requestInterface';

class RequestDetails {

    protected request: IRequest;

    constructor (request: IRequest) {
        this.request = request;
    }
}

export = RequestDetails
