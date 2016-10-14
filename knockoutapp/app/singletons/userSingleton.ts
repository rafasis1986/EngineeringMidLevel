import {getSession, setSession} from "../services/utils";
import {Constant} from "../constants/enviroment";

class UserSingleton {

    private static _instance: UserSingleton = new UserSingleton();

    private email: string = null;

    private full_name: string = null;

    private roles: string = null;

    constructor() {
        if(UserSingleton._instance){
            throw new Error("Error: Instantiation failed: Use UserSingleton.getInstance() instead of new.");
        }
        UserSingleton._instance = this;
    }

    public static getEmail(): string{
        return getSession(Constant.SESSION_EMAIL);
    }

    public static setEmail(value: string): void{
        setSession(Constant.SESSION_EMAIL, value);
    }

    public static getFullName(): string{
        return getSession(Constant.SESSION_FULL_NAME);
    }

    public static setFullName(value: string): void{
        setSession(Constant.SESSION_FULL_NAME, value);
    }

    public static getRoles(): string{
        return getSession(Constant.SESSION_ROLES);
    }

    public static setRoles(value: string): void{
        setSession(Constant.SESSION_ROLES, value);
    }

}

export {UserSingleton};
