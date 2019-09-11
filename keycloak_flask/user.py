import json
import logging

from flask import Flask, request, render_template, redirect, flash, url_for
from flask import session, make_response, g

from keycloak_flask.forms import RegistrationForm, LoginForm
from keycloak_flask.keycloak_utils import get_admin, create_user, get_oidc, get_token, check_token


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object('keycloak_flask.settings')
app.config.from_envvar('KEYCLOAK_FLASK_SETTINGS')


@app.before_request
def load_user():
    g.username = session.get('username')
    g.access_token = session.get('access_token')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        oidc_obj = get_oidc()
        token = get_token(oidc_obj, form.username.data, form.password.data)
        print("\nTOKEN: %s\n" % token)
        response = make_response(redirect(url_for('home')))
        if token:
            response.set_cookie('access_token', token['access_token'])
            session['access_token'] = token['access_token']
            session['username'] = form.username.data
        return response
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('access_token', None)
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        admin = get_admin()
        create_user(admin, form.username.data, form.email.data, form.password.data)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/headers')
def headers():
    return dict(request.headers)


@app.route('/protected')
def protected():
    resp = 'Forbidden!'
    access_token = session.get('access_token')
    if access_token:
        if check_token(access_token):
            headers = dict(request.headers)
            resp = 'Protected resource is accessible. Yay! Here is the Authorization HEADER: %s' % str(headers.get('Authorization'))
    return resp
