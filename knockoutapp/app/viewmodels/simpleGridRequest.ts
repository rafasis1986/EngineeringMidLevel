import * as ko from 'knockout';
import * as app from 'durandal/app';
import SimpleGrid = require('./simpleGrid');
import CustomDialog = require('./customModal');
import {IRequest} from 'requestInterface';
import {getRequestDetails} from '../services/requestServices';
import RequestDetails = require('./requestDetails');


class SimpleGridRequest extends SimpleGrid {

    public showCustomModal(requestPath: any){
        getRequestDetails(requestPath)
            .then((request: IRequest) => {
                this.dialog = new CustomDialog(request.title, new RequestDetails(request));
                this.dialog.show();})
            .catch((error: Error) => {
                console.log(error.toString());
            });
    }
}
export = SimpleGridRequest;



