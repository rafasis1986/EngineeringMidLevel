import {IClient} from 'clientInterfaces';

class ClientDetails {

    protected client: IClient;
    protected affiliateDay: string;

    constructor (client: IClient) {
        this.client = client;
        this.affiliateDay = this.client.created_at.split('T')[0];
    }
}

export = ClientDetails
