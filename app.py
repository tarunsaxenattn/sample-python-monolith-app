from flask import Flask, render_template, request
from flask import url_for
from bandsintown import Client
from healthcheck import HealthCheck, EnvironmentDump
import requests
import urllib
import os

app = Flask(__name__)
## Checking env vars
print (os.environ)

## Setting healthcheckhost environement var
# Set default healthcheckhost = os.environ.get('healthcheckhost', '127.0.0.1')

healthcheckhost = os.environ.get('healthcheckhost')

health = HealthCheck(app, "/healthcheck")

## Login healthcheck function
def login_available():
    r = requests.get(f'http://{healthcheckhost}/login')
    print (r.status_code)
    if r.status_code == 200:
        return True, "Login up @@ "
    else:
        return False, "Login down!!"

## Payment healthcheck function
def payment_available():
    r = requests.get(f'http://{healthcheckhost}/payment')
    print (r.status_code)
    if r.status_code == 200:
        return True, "Payment up @@ "
    else:
        return False, "Payment down!!"


## Registering healthcheck endpoints to /healthcheck api
health.add_check(login_available)
health.add_check(payment_available)

## Defining routes
@app.route('/')
def index():
    return 'UI'

@app.route('/login')
def login():
    return 'login page'

@app.route('/payment')
def payment():
    return 'payment page'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)