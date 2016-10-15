import {getSession, setSession} from '../services/utils';
import {Constant} from '../constants/enviroment';


export function getUserEmail(): string{
    return getSession(Constant.SESSION_EMAIL);
}

export function setUserEmail(value: string): void{
    setSession(Constant.SESSION_EMAIL, value);
}

export function getUserFullName(): string{
    return getSession(Constant.SESSION_FULL_NAME);
}

export function setUserFullName(value: string): void{
    setSession(Constant.SESSION_FULL_NAME, value);
}

export function getUserRoles(): string{
    return getSession(Constant.SESSION_ROLES);
}

export function setUserRoles(value: string): void{
    setSession(Constant.SESSION_ROLES, value);
}
