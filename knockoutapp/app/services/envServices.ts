/**
 * Created by rtorres on 9/24/16.
 */
import {getCookie} from './utils';

import {Constant} from '../constants/enviroment';


export function getEnv(): string {
    let env: string = getCookie(Constant.ENV_LABEL);
    if (! env){
        return Constant.DEVELOPMENT_ENV;
    }
    return env;
}

