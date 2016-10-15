import * as ko from 'knockout';
import * as app from 'durandal/app';
import ClientDetails = require('../viewmodels/clientDetails');
import SimpleGrid = require('./simpleGrid');
import CustomDialog = require('./customModal');
import Existing = require('../viewmodels/clientDetails');
import {IClient} from 'clientInterfaces';
import {getClientDetails} from '../services/clientServices';


class SimpleGridClient extends SimpleGrid {

    protected checkName: any = ko.observable(true);
    protected checkId: any = ko.observable(true);
    protected checkEmail: any = ko.observable(true);

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

    public filterCompare(item: any): boolean {
        let flag: boolean = false,
            filter: string = this.currentFilter().toUpperCase();

        if (this.checkName() && item.full_name.toUpperCase().indexOf(filter) != -1) {
            flag = true;
        }
        else if ( this.checkId() && item.id.toString().indexOf(filter) != -1) {
            flag = true;
        }
        else if ( this.checkEmail() && item.email.toUpperCase().indexOf(filter) != -1) {
            flag = true;
        }
        else if (! (this.checkId() || this.checkName() || this.checkEmail())){
            flag = true;
        }
        return flag;
    }
}

export = SimpleGridClient;



