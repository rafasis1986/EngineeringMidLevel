/**
 * Created by rtorres on 9/24/16.
 */

export class Constant {
    public static get AREAS_API(): string { return 'utils_areas'; };
    public static get AUTH_LABEL(): string { return 'Authorization'; };
    public static get AUTH_PATH(): string { return '/auth'; };
    public static get AUTH_PATH_LABEL(): string { return 'auth'; };
    public static get CHARACTER_PARTITION(): string { return '\\073'; };
    public static get CLIENTS_API(): string { return 'client_list'; };
    public static get DEVELOPMENT_ENV(): string { return 'dev'; };
    public static get DEVELOPMENT_BE_URL(): string { return 'http://localhost:5000'; };
    public static get ENV_LABEL(): string { return 'Env'; };
    public static get MESSAGE(): string { return 'message'; };
    public static get MESSAGE_CONTENT(): string { return 'message_content'; };
    public static get MESSAGE_TYPE(): string { return 'message_type'; };
    public static get PAGINATE_LIMIT(): number { return 10; };
    public static get PENDINGS_API(): string { return 'pending_list'; };
    public static get PRODUCTION_ENV(): string { return 'prod'; };
    public static get PRODUCTION_BE_URL(): string { return 'http://rtorres.info.ve'; };
    public static get REQUESTS_API(): string { return 'request_list'; };
    public static get TICKETS_API(): string { return 'tickets_list'; };
    public static get TYPE_TOKEN(): string { return 'Bearer'; };
    public static get ROLE_CLIENT(): string { return 'client'; };
    public static get ROLE_EMPLOYEE(): string { return 'employee'; };
    public static get SESSION_FULL_NAME(): string { return 'full_name'; };
    public static get SESSION_EMAIL(): string { return 'email'; };
    public static get SESSION_PROFILE_PICTURE(): string { return 'profile_picture'; };
    public static get SESSION_ROLES(): string { return 'roles'; };
    public static get USERS_API(): string { return 'user_list'; };
    public static get USERS_API_ME(): string { return 'me'; };
    public static get URLS_LABEL(): string { return 'urls'; };
}
