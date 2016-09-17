/// <amd-dependency path="text!./home.html" />
import ko = require("knockout");
export var template: string = require("text!./home.html");

export class viewModel {
    public message = ko.observable("Welcome to ko-t!");

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
