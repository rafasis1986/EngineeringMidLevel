/// <amd-dependency path="text!./login.html" />
import ko = require("knockout");
export var template: string = require("text!./login.html");

export const API_URL = ' http://localhost:5000/api/1.0/';

export class viewModel {
    
    public message: any = ko.observable('');
    public userPassword: any = ko.observable();
    public userEmail: any = ko.observable();
    public erroMessage: any = ko.observable();
    public isVisible: any = ko.observable(true);

    constructor(params: any) {
        let aux: string = sessionStorage.getItem('token');
        if (aux) {
            this.isVisible(false);
        }
    }

    public goSignUp(): void {
        window.location.assign('#sign-up');
    }

    public login(): void {
        $.ajax( API_URL + '/auth/', {
            method: 'POST',
            data: {
                email: this.userEmail,
                password: this.userPassword
            }
        }).then((data: any) => {
            console.log(data);
        }).fail((error: Error) => {
            this.erroMessage(error);
        });
    }

    public doSomething() {
        let root: string = 'http://jsonplaceholder.typicode.com';
        var response= '';

        $.ajax( root + '/posts', {
            method: 'POST',
            data: {
                title: 'foo',
                body: 'bar',
                userId: 1
            }
        }).then((data: any) => {
            console.log(data);
            
            $.ajax({
            url: root + '/posts/1',
            method: 'GET'}
            )
            .then((data: any) => {
                console.log(data);
                this.message(data.title);
            })
            .fail((error: Error) => {
                console.log(error);
            });
        });
    }
}
