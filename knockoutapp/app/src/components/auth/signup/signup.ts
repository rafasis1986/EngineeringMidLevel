///<reference path="../../../../typings/globals/jquery/index.d.ts"/>
/// <amd-dependency path="text!./signup.html" />
import * as ko from 'knockout';

let template: any = require('text!./signup.html');
const API_URL = ' http://localhost:5000/api/1.0/';

export class viewModel {

    public userPassword: any = ko.observable();
    public userName: any = ko.observable();
    public userEmail: any = ko.observable();
    public erroMessage: any = ko.observable();
    public isVisible: any = ko.observable(true);

    constructor(params: any) {
        let aux: string = sessionStorage.getItem('token');
        if (aux) {
            this.isVisible(false);
        }
    }

    public signUp(): void {
        $.ajax( API_URL + 'users/', {
            method: 'POST',
            data: {
                username: this.userName,
                email: this.userEmail,
                password: this.userPassword
            }
        }).then((data: any) => {
            console.log(data);
        }).fail((error: Error) => {
            this.erroMessage(error);
        });
    }
}

export  {template}
