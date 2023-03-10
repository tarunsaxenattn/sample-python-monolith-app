from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Sample monolith python application'
@app.route('/payment')
def payment():
    return 'Payment Service is healthy'

@app.route('/login')
def login():
    return 'Login Service is healthy'

@app.route('/ui')
def ui():
    return 'UI Service is healthy'

@app.route('/health')
def health():
    return 'app is healthy'
if __name__ == '__main__':
    app.run(host='0.0.0.0')
