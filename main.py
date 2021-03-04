from flask import Flask 

from markupsafe import escape
from dev import DevConfig

app = Flask(__name__)
app.dev['SQLAlchmy_DATABASE_URL'](DevConfig)


@app.route('/')
def index():
    return '<h1>Site</h1>'
    self.email = email
    self.password = db.Column(db.String(255))

@app.route('/')
def hello():
    
    return 'Alô Mundo!'

@app.route('/login')
def login():
    return 'login'

@app.route('/todo')
def todo():
    return '<h1>Corpo</h1>'


@app.route('/user/<jeffe_user>')
def profile(username):
    return '{}\'s profile'.format(escape())

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/user2/<path:subpath>')
def show_subpath(subpath):
    return '<h2>Subpath %s</h2>' % escape(subpath)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Jeffe user'))

if __name__ == '__main__':
    app.run(host='127.0.0.1')