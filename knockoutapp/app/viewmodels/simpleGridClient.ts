import * as ko from 'knockout';
import * as app from 'durandal/app';
import ClientDetails = require('./clientDetails');
import SimpleGrid = require('./simpleGrid');
import CustomDialog = require('./customModal');
import Existing = require('./clientDetails');
import {Constant} from '../constants/enviroment';
import {IClient} from 'clientInterfaces';
import {getClientDetails} from '../services/clientServices';


class SimpleGridClient extends SimpleGrid {

    protected dialog: any = null;

    public showCustomModal(clientPath: any){
        let clientInfo: IClient;
        getClientDetails(clientPath)
            .then((client: IClient) => {
                clientInfo = client;
                this.dialog = new CustomDialog('Client Details', new ClientDetails(clientInfo));
                this.dialog.show();})
            .catch((error: Error) => {
                console.log(error.toString());
            })
    }




}

export = SimpleGridClient;



