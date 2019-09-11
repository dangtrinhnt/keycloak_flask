from keycloak import KeycloakAdmin, KeycloakOpenID
from flask import current_app


def get_admin():
    return KeycloakAdmin(server_url=current_app.config.get('SERVER_URL'),
                         username=current_app.config.get('ADMIN_USERNAME'),
                         password=current_app.config.get('ADMIN_PASS'),
                         realm_name=current_app.config.get('REALM_NAME'),
                         verify=True)


def create_user(admin, username, email, password):
    return admin.create_user({"email": email,
                              "username": username,
                              "credentials": [{"value": password,"type": "password",}],
                              "enabled": True,
                              "realmRoles": ["user",]})


def get_oidc():
    return KeycloakOpenID(server_url=current_app.config.get('SERVER_URL'),
                          client_id=current_app.config.get('CLIENT_ID'),
                          realm_name=current_app.config.get('REALM_NAME'),
                          client_secret_key=current_app.config.get('CLIENT_SECRET'),
                          verify=True)


def get_token(oidc_obj, username, password):
    try:
        return oidc_obj.token(username, password)
    except Exception as e:
        print("Exception occurs: %s" % e)
    return None


def check_token(access_token):
    oidc = get_oidc()
    token_info = oidc.introspect(access_token)
    if token_info.get('active'):
        return True
    return False


def get_userinfo(access_token):
    oidc = get_oidc()
    try:
        return oidc.userinfo(access_token)
    except Exception as e:
        print("Exception occurs: %s" % e)
    return None
