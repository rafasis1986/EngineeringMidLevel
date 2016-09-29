import * as ko from 'knockout';
import {Constant} from '../constants/enviroment';

import * as app from 'durandal/app';
class SimpleGrid {

    protected data: any = ko.observableArray();
    protected currentPageIndex: any  = ko.observable(0);
    protected pageSize: number =  Constant.PAGINATE_LIMIT;
    protected columns: any = [];
    protected itemsOnCurrentPage;
    protected maxPageIndex: any;

    constructor (data?: any[], colums?: any[], pageSize?: number) {
        this.data = data || null;
        this.columns = colums || [];
        this.pageSize = pageSize || this.pageSize;
        this.itemsOnCurrentPage = ko.computed(() => {
            let startIndex = this.pageSize * this.currentPageIndex();
            return this.data.slice(startIndex, startIndex + this.pageSize);
        });
        this.maxPageIndex = ko.computed(() => {
            return Math.ceil(ko.utils.unwrapObservable(this.data).length / this.pageSize) -1;
        });
    }

    public setData(data: any[]) {
        this.data = data;
    }

    public getData(): any {
        return this.data;
    }

    public setColumns(columns: any[]) {
        this.columns = columns;
    }

    public getColumns(): any[] {
        return this.columns;
    }

    public setPageSize(pageSize: number) {
        this.pageSize = pageSize;
    }

    public getPageSize(): number {
        return this.pageSize;
    }

    public setCurrentPageIndex(pageIndex: number) {
        this.currentPageIndex = pageIndex;
    }

    public getCurrentPageIndex(): number {
        return this.currentPageIndex;
    }

    public getColumnsForScaffolding(data: any): any {
        if ((typeof data.length !== 'number') || data.length === 0) {
            return [];
        }
        let columns = [];
        for (var propertyName in data[0]) {
            columns.push({ headerText: propertyName, rowText: propertyName });
        }
        return columns;
    }

    public viewDetail(clientData: any) {
        console.log(clientData);
        return app.showMessage(clientData, clientData);
    }

}

export = SimpleGrid;



