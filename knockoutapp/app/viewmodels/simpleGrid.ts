import * as ko from 'knockout';
import * as app from 'durandal/app';
import {Constant} from '../constants/enviroment';

class SimpleGrid {

    protected data: any = ko.observableArray();
    protected currentPageIndex: any  = ko.observable(0);
    protected pageSize: number =  Constant.PAGINATE_LIMIT;
    protected columns: any = [];
    protected itemsOnCurrentPage;
    protected maxPageIndex: number;

    constructor (data: any[], colums?: any[], pageSize?: number) {
        this.data(data);
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

    public getMaxPageIndex(): number {
        return this.maxPageIndex;
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

    public viewDetail(clientData: any, data: any, event: any): any {
        console.log(clientData);
        console.log(data);
        console.log(event);
        return app.showMessage(clientData, clientData);
    }

    public jumpToFirstPage(): void {
        this.currentPageIndex = 0;
    }

    public jumpToLastPage(): void {
        this.currentPageIndex = this.maxPageIndex;
    }

    public sortBy(key: string, order: string): void {
        if (order == 'asc'){
            this.data.sort((a, b) => {
                return a[key] < b[key] ? -1 : 1;
            });
        } else {
            this.data.sort((a, b) => {
                return a[key] < b[key] ? 1 : -1;
            });
        }
    }

}

export = SimpleGrid;



