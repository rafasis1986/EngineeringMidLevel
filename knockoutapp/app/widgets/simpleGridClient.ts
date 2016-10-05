import * as ko from 'knockout';
import * as app from 'durandal/app';
import ClientDetails = require('../viewmodels/clientDetails');
import SimpleGrid = require('./simpleGrid');
import CustomDialog = require('./customModal');
import Existing = require('../viewmodels/clientDetails');
import {IClient} from 'clientInterfaces';
import {getClientDetails} from '../services/clientServices';


class SimpleGridClient extends SimpleGrid {

    public showCustomModal(clientPath: any){
        let clientInfo: IClient;
        getClientDetails(clientPath)
            .then((client: IClient) => {
                clientInfo = client;
                this.dialog = new CustomDialog('Client Details', new ClientDetails(clientInfo));
                this.dialog.show();})
            .catch((error: Error) => {
                console.log(error.toString());
            });
    }
}

export = SimpleGridClient;



