# for local
# It's probably helpful for us to demonstrate what the URL should be, etc.

SECRET_KEY = b'keycloak'

# http, not https for some reason
SERVER_URL = "http://keycloak-idp:8080/auth/"
ADMIN_USERNAME = "admin"
ADMIN_PASS = "admin"
REALM_NAME = "master"
# created in keycloak per https://github.com/keycloak/keycloak-documentation/blob/main/securing_apps/topics/client-registration/client-registration-cli.adoc
CLIENT_ID = "keycloak-flask"
CLIENT_SECRET = ""

INGRESS_HOST = "https://www.google.com/"
