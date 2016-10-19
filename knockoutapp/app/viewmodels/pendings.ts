import * as ko from 'knockout';
import * as system from 'durandal/system';
import * as app from 'durandal/app';
import * as Q from 'q';
import Deferred = Q.Deferred;
import {IRequest} from 'requestInterface';
import SimpleGridRequest = require('../widgets/simpleGridRequest');
import {getPendingRequests} from '../services/requestServices';
import {IRequestBase} from 'requestInterface';
import BaseView = require('./baseView');
import * as userSession from '../singletons/userSession';
import {Constant} from '../constants/enviroment';
import {INode} from 'treeNodeInterfaces';

const columns = [{ headerText: 'Id', rowText: 'id' },
    { headerText: 'Title', rowText: 'title' },
    { headerText: 'Client', rowText: 'client_id' },
    { headerText: 'Priority', rowText: 'client_priority' },
    { headerText: 'Area', rowText: 'product_area' },
    { headerText: 'Target Date', rowText: 'target_date' },
    { headerText: 'Attended', rowText: 'attended' },
    { headerText: 'Details', rowText: 'link' },
];

class Pendings extends BaseView {

    private pendings: any[];
    private pendingsArray: any = ko.observableArray();
    private isLoading: any = ko.observable();
    private isClient: any = ko.observable(false);

    public activate() {
        this.isLoading(true);

        if (userSession.getUserRoles().search(Constant.ROLE_CLIENT) != -1) {
            this.isClient(true);
        }
        return  this.loadPendings().then((data) => {
                this.pendings = data;
                this.pendingsArray(data);
                this.isLoading(false);
        });
    }

    public attached() {
        this.pendings.reverse();
        let root: INode,
            i: number = 0;
        for(i; i<this.pendings.length ; i++) {
            let auxNode: INode = {
                text : this.pendings[i].id + ': '  + this.pendings[i].title,
                href : '#pendig' + this.pendings[i].id,
                tags : [ '' + this.pendings[i].client_priority]};
            if ( i>0 ){
                auxNode.nodes = [root];
            }
            root = auxNode;
        }
        $('#tree').treeview({
            expandIcon: 'glyphicon glyphicon-menu-right',
            collapseIcon: 'glyphicon glyphicon-menu-up',
            nodeIcon: 'glyphicon glyphicon-tasks',
            showTags: true,
            data: [root]});

    }

    public loadPendings(): JQueryDeferred<IRequestBase[]> {
        return system.defer((dfd) => {
            setTimeout( () => {
                getPendingRequests().then((requests: IRequest[]) => {
                    dfd.resolve(requests); })
                    .catch((err: Error) => {
                        window.location.assign('#');
                    });
            }, 500);
        });
    }
}

export = Pendings;
