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
# set access-type to confidential, save, reload, will see a credentials tab where you can set this
CLIENT_SECRET = "2da4a9a4-f6f0-48d9-82f6-12012402f03a"

INGRESS_HOST = "http://www.google.com/"
