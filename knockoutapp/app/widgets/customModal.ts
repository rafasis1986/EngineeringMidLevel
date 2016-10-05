import * as dialog from 'plugins/dialog';

class CustomModal {

    protected title: string;
    protected model: any;

    constructor (title: string, model: any){
        this.title = title;
        this.model = model;
    }

    public close () {
        dialog.close(this, this.model);
    }

    public show () {
        return dialog.show(this);
    }
}

export = CustomModal;
